#!/usr/bin/env python3
"""
Script to add timestamps to agent chat log markdown files
"""
import os
import json
from datetime import datetime
from pathlib import Path

# Paths
cursor_transcripts = Path.home() / '.cursor/projects/Users-kylemathewson-mathTest/agent-transcripts'
repo_prompt_history = Path('/Users/kylemathewson/mathTest/promptHistory')

# Create timestamp metadata file
timestamp_data = {}

print("Processing agent transcripts...")

# Get all transcript files with their timestamps
for txt_file in sorted(cursor_transcripts.glob('*.txt')):
    # Get file modification time
    mod_time = os.path.getmtime(txt_file)
    timestamp = datetime.fromtimestamp(mod_time)
    
    file_id = txt_file.stem
    md_file = repo_prompt_history / f"{file_id}.md"
    
    # Read the transcript content
    with open(txt_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create header with metadata
    header = f"""---
agent_id: {file_id}
timestamp: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}
date: {timestamp.strftime('%B %d, %Y')}
time: {timestamp.strftime('%I:%M %p')}
last_modified: {timestamp.isoformat()}
---

# Agent Chat Log
**Session ID:** `{file_id}`  
**Date:** {timestamp.strftime('%B %d, %Y')}  
**Time:** {timestamp.strftime('%I:%M:%S %p')}

---

"""
    
    # Write to markdown file with header
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(header + content)
    
    # Store metadata
    timestamp_data[file_id] = {
        'timestamp': timestamp.isoformat(),
        'date': timestamp.strftime('%Y-%m-%d'),
        'time': timestamp.strftime('%H:%M:%S'),
        'display_date': timestamp.strftime('%B %d, %Y'),
        'display_time': timestamp.strftime('%I:%M %p'),
        'size': os.path.getsize(txt_file),
        'file': f"{file_id}.md"
    }
    
    print(f"✓ {file_id}.md - {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

# Save metadata as JSON
metadata_file = repo_prompt_history / 'timestamps.json'
with open(metadata_file, 'w', encoding='utf-8') as f:
    json.dump(timestamp_data, f, indent=2, sort_keys=True)

print(f"\n✓ Created {metadata_file}")
print(f"\nTotal files processed: {len(timestamp_data)}")
print("\nFiles sorted by date (oldest to newest):")
sorted_files = sorted(timestamp_data.items(), key=lambda x: x[1]['timestamp'])
for file_id, data in sorted_files:
    print(f"  {data['display_date']} {data['display_time']} - {file_id}")
