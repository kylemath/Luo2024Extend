#!/usr/bin/env python3
"""
Enhanced PDF to Markdown Converter with LaTeX Equation Extraction
Converts academic papers from PDF to Markdown format with proper LaTeX equations
"""

import fitz  # PyMuPDF
import re
import sys
from pathlib import Path


def extract_text_from_pdf(pdf_path):
    """Extract text from PDF preserving structure."""
    doc = fitz.open(pdf_path)
    full_text = []
    
    for page in doc:
        text = page.get_text()
        full_text.append(text)
    
    doc.close()
    return '\n'.join(full_text)


def convert_special_chars_to_latex(text):
    """Convert special mathematical characters to LaTeX commands."""
    replacements = {
        '∈': r'\in',
        '∑': r'\sum',
        '∏': r'\prod',
        '∫': r'\int',
        '∂': r'\partial',
        '≤': r'\leq',
        '≥': r'\geq',
        '≠': r'\neq',
        '≈': r'\approx',
        '→': r'\to',
        '⇒': r'\Rightarrow',
        '⇐': r'\Leftarrow',
        '⇔': r'\Leftrightarrow',
        '⊂': r'\subset',
        '⊆': r'\subseteq',
        '∪': r'\cup',
        '∩': r'\cap',
        '×': r'\times',
        '∆': r'\Delta',
        '∇': r'\nabla',
        '∞': r'\infty',
        '∅': r'\emptyset',
        '∀': r'\forall',
        '∃': r'\exists',
        '∧': r'\land',
        '∨': r'\lor',
        '¬': r'\neg',
        '≿': r'\succeq',
        '≻': r'\succ',
        '≺': r'\prec',
        '⊃': r'\supset',
        '⊇': r'\supseteq',
        '̸=': r'\neq',
        '̸': '',  # Combining character
        'α': r'\alpha',
        'β': r'\beta',
        'γ': r'\gamma',
        'δ': r'\delta',
        'ε': r'\varepsilon',
        'ζ': r'\zeta',
        'η': r'\eta',
        'θ': r'\theta',
        'λ': r'\lambda',
        'μ': r'\mu',
        'ν': r'\nu',
        'π': r'\pi',
        'ρ': r'\rho',
        'σ': r'\sigma',
        'τ': r'\tau',
        'φ': r'\phi',
        'χ': r'\chi',
        'ψ': r'\psi',
        'ω': r'\omega',
        'Γ': r'\Gamma',
        'Δ': r'\Delta',
        'Θ': r'\Theta',
        'Λ': r'\Lambda',
        'Π': r'\Pi',
        'Σ': r'\Sigma',
        'Φ': r'\Phi',
        'Ψ': r'\Psi',
        'Ω': r'\Omega',
    }
    
    for char, latex in replacements.items():
        text = text.replace(char, latex)
    
    return text


def is_equation_line(line):
    """Detect if a line is likely an equation."""
    # Strip whitespace
    line = line.strip()
    
    # Empty lines are not equations
    if not line:
        return False
    
    # Check for LaTeX commands
    if '\\' in line and any(cmd in line for cmd in ['sum', 'int', 'prod', 'alpha', 'beta', 'gamma', 'delta', 'theta', 'lambda', 'mu', 'sigma', 'omega', 'in', 'leq', 'geq']):
        return True
    
    # Check for mathematical operators and symbols
    math_symbols = ['=', '≤', '≥', '∈', '∑', '∏', '∫', '∂', '×', '→', '⇒', '⇔']
    has_math_symbol = any(sym in line for sym in math_symbols)
    
    # Check for variable patterns (subscripts, superscripts, etc.)
    has_math_pattern = bool(re.search(r'[a-zA-Z][_\^]|[a-zA-Z]\s*[=<>]|\([a-zA-Z0-9,\s]+\)|max|min|sup|inf|lim|arg', line))
    
    # Lines that are mostly mathematical
    words = line.split()
    if len(words) <= 10 and (has_math_symbol or has_math_pattern):
        # Check if it's not a regular sentence
        if not any(word.lower() in ['the', 'is', 'are', 'was', 'were', 'a', 'an', 'this', 'that', 'these', 'those'] for word in words):
            return True
    
    return False


def extract_equations(text):
    """Extract standalone equations from text."""
    lines = text.split('\n')
    equations = []
    current_equation = []
    in_equation = False
    
    for line in lines:
        if is_equation_line(line):
            current_equation.append(line.strip())
            in_equation = True
        else:
            if in_equation and current_equation:
                equations.append(' '.join(current_equation))
                current_equation = []
            in_equation = False
    
    # Add last equation if any
    if current_equation:
        equations.append(' '.join(current_equation))
    
    return equations


def format_markdown(text):
    """Format text as markdown with proper structure."""
    lines = text.split('\n')
    markdown = []
    
    # Process title and metadata
    title_found = False
    for i, line in enumerate(lines[:20]):
        line = line.strip()
        if not line:
            continue
        
        if not title_found and len(line) < 100:
            markdown.append(f"# {line}\n")
            title_found = True
        elif i < 10 and len(line) < 80 and not line.endswith('.'):
            markdown.append(f"**{line}**\n")
        else:
            break
    
    # Process main content
    in_paragraph = False
    paragraph_lines = []
    
    for i, line in enumerate(lines[10:], 10):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            if paragraph_lines:
                markdown.append(' '.join(paragraph_lines) + '\n')
                paragraph_lines = []
                in_paragraph = False
            markdown.append('')
            continue
        
        # Check for section headers
        if re.match(r'^\d+\.?\s+[A-Z]', line) or (line.isupper() and len(line.split()) <= 6):
            if paragraph_lines:
                markdown.append(' '.join(paragraph_lines) + '\n')
                paragraph_lines = []
            markdown.append(f"\n## {line}\n")
            in_paragraph = False
            continue
        
        # Check for equations
        if is_equation_line(line):
            if paragraph_lines:
                markdown.append(' '.join(paragraph_lines) + '\n')
                paragraph_lines = []
            markdown.append(f"\n$$\n{line}\n$$\n")
            in_paragraph = False
            continue
        
        # Regular text - accumulate into paragraph
        paragraph_lines.append(line)
        in_paragraph = True
    
    # Add any remaining paragraph
    if paragraph_lines:
        markdown.append(' '.join(paragraph_lines))
    
    return '\n'.join(markdown)


def create_equations_file(text, output_path):
    """Create a separate LaTeX file with all equations."""
    equations = extract_equations(text)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("% LaTeX Equations extracted from PDF\n")
        f.write("% Compile with pdflatex or similar\n\n")
        f.write("\\documentclass{article}\n")
        f.write("\\usepackage{amsmath}\n")
        f.write("\\usepackage{amssymb}\n")
        f.write("\\usepackage{amsthm}\n\n")
        f.write("\\begin{document}\n\n")
        f.write("\\section*{Equations}\n\n")
        
        for i, eq in enumerate(equations, 1):
            f.write(f"% Equation {i}\n")
            f.write("\\begin{equation}\n")
            f.write(f"{eq}\n")
            f.write("\\end{equation}\n\n")
        
        f.write("\\end{document}\n")
    
    return len(equations)


def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_pdf_to_md_v2.py <pdf_file>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    
    if not Path(pdf_path).exists():
        print(f"Error: File '{pdf_path}' not found")
        sys.exit(1)
    
    print(f"Converting {pdf_path} to Markdown...")
    
    # Extract text from PDF
    raw_text = extract_text_from_pdf(pdf_path)
    
    # Convert special characters to LaTeX
    text_with_latex = convert_special_chars_to_latex(raw_text)
    
    # Format as markdown
    markdown_content = format_markdown(text_with_latex)
    
    # Generate output filenames
    base_name = Path(pdf_path).stem
    md_output = base_name + '.md'
    tex_output = base_name + '_equations.tex'
    
    # Write markdown file
    with open(md_output, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"✓ Markdown file created: {md_output}")
    print(f"  - Total lines: {len(markdown_content.splitlines())}")
    
    # Create equations file
    num_equations = create_equations_file(text_with_latex, tex_output)
    print(f"✓ LaTeX equations file created: {tex_output}")
    print(f"  - {num_equations} equations extracted")


if __name__ == "__main__":
    main()
