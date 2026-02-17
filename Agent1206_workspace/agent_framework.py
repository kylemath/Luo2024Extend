"""
Agent Framework for Hierarchical Task Decomposition
====================================================

Provides a reusable Agent class that:
- Reads task assignments from .md files
- Delegates to sub-agents via task .md files
- Collects reports from sub-agents
- Produces its own report summarizing sub-agent findings
- Links to generated figures, scripts, and data

Usage:
    agent = Agent("SA1", "SR Beliefs Analysis", "Agent1206_workspace/SA1_SRBeliefs")
    agent.load_task()        # reads task.md
    agent.run_subagents()    # executes all SSA scripts and collects reports
    agent.compile_report()   # produces report.md
"""

import os
import subprocess
import sys
import json
import datetime
from pathlib import Path
from typing import List, Optional, Dict


class Agent:
    """Hierarchical agent that manages task decomposition via .md files."""

    def __init__(self, agent_id: str, name: str, workspace: str,
                 parent_id: Optional[str] = None, level: int = 0):
        self.agent_id = agent_id
        self.name = name
        self.workspace = Path(workspace)
        self.parent_id = parent_id
        self.level = level  # 0 = orchestrator, 1 = subagent, 2 = sub-subagent
        self.subagents: List[Agent] = []
        self.task_text: str = ""
        self.report_text: str = ""
        self.status: str = "pending"  # pending, running, completed, failed
        self.scripts: List[Path] = []
        self.figures: List[Path] = []
        self.start_time: Optional[datetime.datetime] = None
        self.end_time: Optional[datetime.datetime] = None

    @property
    def task_path(self) -> Path:
        return self.workspace / "task.md"

    @property
    def report_path(self) -> Path:
        return self.workspace / "report.md"

    def load_task(self) -> str:
        """Read the task assignment from task.md."""
        if self.task_path.exists():
            self.task_text = self.task_path.read_text()
        return self.task_text

    def discover_subagents(self) -> List['Agent']:
        """Discover sub-agent directories (SSA* folders)."""
        self.subagents = []
        if not self.workspace.exists():
            return self.subagents

        for item in sorted(self.workspace.iterdir()):
            if item.is_dir() and (item.name.startswith("SSA") or
                                   item.name.startswith("SA")):
                sub = Agent(
                    agent_id=item.name,
                    name=item.name,
                    workspace=str(item),
                    parent_id=self.agent_id,
                    level=self.level + 1
                )
                self.subagents.append(sub)
        return self.subagents

    def discover_scripts(self) -> List[Path]:
        """Find all .py scripts in this agent's workspace (not in subdirs)."""
        self.scripts = []
        if self.workspace.exists():
            for f in self.workspace.iterdir():
                if f.is_file() and f.suffix == '.py' and f.name != '__init__.py':
                    self.scripts.append(f)
        return self.scripts

    def discover_figures(self) -> List[Path]:
        """Find all generated figures."""
        self.figures = []
        fig_dir = self.workspace / "figures"
        if fig_dir.exists():
            for f in fig_dir.iterdir():
                if f.suffix in ('.png', '.pdf', '.svg'):
                    self.figures.append(f)
        return self.figures

    def run_script(self, script_path: Path, venv_python: Optional[str] = None,
                   timeout: int = 300) -> Dict:
        """Execute a Python script and capture output."""
        if venv_python is None:
            venv_python = str(
                Path(__file__).parent / "venv" / "bin" / "python"
            )

        env = os.environ.copy()
        env["PYTHONPATH"] = str(Path(__file__).parent)

        result = {
            "script": str(script_path),
            "status": "pending",
            "stdout": "",
            "stderr": "",
            "returncode": -1
        }

        try:
            proc = subprocess.run(
                [venv_python, str(script_path)],
                capture_output=True, text=True, timeout=timeout,
                env=env, cwd=str(self.workspace)
            )
            result["stdout"] = proc.stdout
            result["stderr"] = proc.stderr
            result["returncode"] = proc.returncode
            result["status"] = "completed" if proc.returncode == 0 else "failed"
        except subprocess.TimeoutExpired:
            result["status"] = "timeout"
            result["stderr"] = f"Script timed out after {timeout}s"
        except Exception as e:
            result["status"] = "error"
            result["stderr"] = str(e)

        return result

    def run_subagents(self, venv_python: Optional[str] = None) -> List[Dict]:
        """Run all sub-agents: execute their scripts and collect reports."""
        self.status = "running"
        self.start_time = datetime.datetime.now()
        results = []

        for sub in self.subagents:
            sub.load_task()
            sub.discover_scripts()
            sub.status = "running"

            for script in sub.scripts:
                res = sub.run_script(script, venv_python=venv_python)
                results.append(res)
                print(f"  [{sub.agent_id}] {script.name}: {res['status']}")
                if res["stderr"] and res["status"] != "completed":
                    print(f"    stderr: {res['stderr'][:200]}")

            sub.discover_figures()
            sub.status = "completed" if all(
                r["status"] == "completed" for r in results
            ) else "partial"

        self.end_time = datetime.datetime.now()
        return results

    def read_subagent_reports(self) -> Dict[str, str]:
        """Read all sub-agent report.md files."""
        reports = {}
        for sub in self.subagents:
            if sub.report_path.exists():
                reports[sub.agent_id] = sub.report_path.read_text()
        return reports

    def compile_report(self, extra_content: str = "") -> str:
        """Compile this agent's report from sub-agent reports."""
        lines = [
            f"# Report: {self.name} ({self.agent_id})",
            f"",
            f"**Status:** {self.status}",
            f"**Level:** {'Orchestrator' if self.level == 0 else 'Subagent' if self.level == 1 else 'Sub-subagent'}",
            f"**Parent:** {self.parent_id or 'None (top-level)'}",
            f"**Generated:** {datetime.datetime.now().isoformat()}",
            f"",
            f"## Task",
            f"",
            self.task_text or "*No task loaded*",
            f"",
        ]

        if extra_content:
            lines.extend([f"## Analysis", f"", extra_content, f""])

        # Sub-agent reports
        sub_reports = self.read_subagent_reports()
        if sub_reports:
            lines.extend([f"## Sub-agent Reports", f""])
            for sid, text in sub_reports.items():
                lines.extend([
                    f"### {sid}",
                    f"",
                    text,
                    f"",
                    f"---",
                    f""
                ])

        # Figures
        self.discover_figures()
        if self.figures:
            lines.extend([f"## Generated Figures", f""])
            for fig in self.figures:
                rel = os.path.relpath(fig, self.workspace)
                lines.append(f"![{fig.stem}]({rel})")
            lines.append("")

        self.report_text = "\n".join(lines)
        self.report_path.write_text(self.report_text)
        return self.report_text

    def to_dict(self) -> Dict:
        """Serialize agent state for JSON logging."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "workspace": str(self.workspace),
            "level": self.level,
            "status": self.status,
            "n_subagents": len(self.subagents),
            "n_scripts": len(self.scripts),
            "n_figures": len(self.figures),
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None,
        }

    def __repr__(self):
        indent = "  " * self.level
        s = f"{indent}Agent({self.agent_id}, status={self.status})"
        for sub in self.subagents:
            s += f"\n{sub}"
        return s


def build_hierarchy(base_path: str) -> Agent:
    """Build the full agent hierarchy from the folder structure."""
    base = Path(base_path)
    orchestrator = Agent("Agent1206", "Orchestrator", str(base), level=0)
    orchestrator.load_task()

    for sa_dir in sorted(base.iterdir()):
        if sa_dir.is_dir() and sa_dir.name.startswith("SA"):
            sa = Agent(
                agent_id=sa_dir.name,
                name=sa_dir.name,
                workspace=str(sa_dir),
                parent_id="Agent1206",
                level=1
            )
            sa.load_task()

            for ssa_dir in sorted(sa_dir.iterdir()):
                if ssa_dir.is_dir() and ssa_dir.name.startswith("SSA"):
                    ssa = Agent(
                        agent_id=ssa_dir.name,
                        name=ssa_dir.name,
                        workspace=str(ssa_dir),
                        parent_id=sa.agent_id,
                        level=2
                    )
                    ssa.load_task()
                    ssa.discover_scripts()
                    sa.subagents.append(ssa)

            orchestrator.subagents.append(sa)

    return orchestrator
