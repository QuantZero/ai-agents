"""Tools for file operations, git, and email in the Agent Builder."""

import os
import json
import subprocess
from pathlib import Path
from typing import Optional, Dict, Any
from datetime import datetime

from schemas import AgentIdea, AgentImplementation, RegistryEntry


def get_existing_agents(repo_root: str) -> list[str]:
    """Get list of existing agent names from the repository."""
    agents = []
    repo_path = Path(repo_root)
    
    # Check for agents/ directory (new structure)
    agents_dir = repo_path / "agents"
    if agents_dir.exists():
        for item in agents_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                agents.append(item.name)
    
    # Also check root-level agent directories (legacy structure)
    for item in repo_path.iterdir():
        if item.is_dir() and item.name.endswith('-agent') and item.name != 'agent-builder-agent':
            agents.append(item.name)
    
    return agents


def create_agent_directory(repo_root: str, date: str, slug: str) -> str:
    """Create directory for new agent: agents/YYYY-MM-DD-agent-name/"""
    agents_dir = Path(repo_root) / "agents"
    agents_dir.mkdir(exist_ok=True)
    
    agent_dir = agents_dir / f"{date}-{slug}"
    agent_dir.mkdir(exist_ok=True)
    
    return str(agent_dir)


def write_agent_files(agent_dir: str, implementation: AgentImplementation) -> bool:
    """Write all agent files to disk."""
    try:
        agent_path = Path(agent_dir)
        
        # Write agent.py
        (agent_path / "agent.py").write_text(implementation.agent_code)
        
        # Write optional files
        if implementation.schemas_code:
            (agent_path / "schemas.py").write_text(implementation.schemas_code)
        
        if implementation.prompts_code:
            (agent_path / "prompts.py").write_text(implementation.prompts_code)
        
        if implementation.graph_code:
            (agent_path / "graph.py").write_text(implementation.graph_code)
        
        if implementation.tools_code:
            (agent_path / "tools.py").write_text(implementation.tools_code)
        
        # Write pyproject.toml
        (agent_path / "pyproject.toml").write_text(implementation.pyproject_toml)
        
        # Write README.md
        (agent_path / "README.md").write_text(implementation.readme_content)
        
        # Write .env.example if provided
        if implementation.env_example:
            (agent_path / ".env.example").write_text(implementation.env_example)
        
        return True
    except Exception as e:
        print(f"Error writing files: {e}")
        return False


def update_registry_readme(registry_path: str, entry: RegistryEntry, existing_content: str) -> str:
    """Update the registry README with a new entry."""
    # Find the "Available Agents" section
    lines = existing_content.split('\n')
    new_lines = []
    in_agents_section = False
    inserted = False
    
    for i, line in enumerate(lines):
        new_lines.append(line)
        
        # Look for "## Available Agents" or similar
        if line.startswith('##') and ('Available' in line or 'Agents' in line):
            in_agents_section = True
            continue
        
        # Insert new entry after the section header, before first existing agent
        if in_agents_section and not inserted:
            if line.startswith('###') or line.startswith('##'):
                # Insert before this agent entry
                new_lines.insert(-1, f"\n### {entry.name}")
                new_lines.insert(-1, f"\n{entry.description}")
                new_lines.insert(-1, f"\n**Category:** {entry.category}")
                new_lines.insert(-1, f"\n**Date:** {entry.date}")
                new_lines.insert(-1, f"\n[📖 Read the {entry.name} README]({entry.link})")
                new_lines.insert(-1, "")
                inserted = True
    
    # If we didn't find a good spot, append to end
    if not inserted:
        new_lines.append(f"\n### {entry.name}")
        new_lines.append(f"\n{entry.description}")
        new_lines.append(f"\n**Category:** {entry.category}")
        new_lines.append(f"\n**Date:** {entry.date}")
        new_lines.append(f"\n[📖 Read the {entry.name} README]({entry.link})")
    
    return '\n'.join(new_lines)


def git_commit_and_push(repo_root: str, agent_name: str, date: str) -> tuple[bool, str]:
    """Commit and push changes to GitHub."""
    try:
        repo_path = Path(repo_root)
        os.chdir(repo_path)
        
        # Check if git is initialized
        if not (repo_path / ".git").exists():
            return False, "Git repository not initialized"
        
        # Add all changes
        subprocess.run(["git", "add", "."], check=True, capture_output=True)
        
        # Commit
        commit_message = f"Daily AI Agent {date}: {agent_name}"
        result = subprocess.run(
            ["git", "commit", "-m", commit_message],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            if "nothing to commit" in result.stdout.lower():
                return False, "No changes to commit"
            return False, f"Commit failed: {result.stderr}"
        
        # Push
        push_result = subprocess.run(
            ["git", "push"],
            capture_output=True,
            text=True
        )
        
        if push_result.returncode != 0:
            return False, f"Push failed: {push_result.stderr}"
        
        return True, "Successfully committed and pushed"
    
    except subprocess.CalledProcessError as e:
        return False, f"Git operation failed: {str(e)}"
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"


def send_email(email_content: str, recipient: Optional[str] = None) -> bool:
    """Send email using system mail command or SMTP.
    
    Hardcoded recipient: jamesdev0101@gmail.com
    """
    # Hardcoded developer email address
    recipient = recipient or "jamesdev0101@gmail.com"
    
    try:
        # Try using system mail command (Unix/Mac)
        process = subprocess.Popen(
            ["mail", "-s", email_content.split('\n')[0].replace("Subject: ", ""), recipient],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        body = '\n'.join(email_content.split('\n')[1:])
        stdout, stderr = process.communicate(input=body)
        
        if process.returncode == 0:
            return True
        else:
            print(f"Mail command failed: {stderr}")
            print("\nEmail content (manual send required):")
            print("\n" + "="*60)
            print(email_content)
            print("="*60)
            return False
    
    except FileNotFoundError:
        # mail command not available, just print
        print("\nEmail content (manual send required):")
        print("\n" + "="*60)
        print(email_content)
        print("="*60)
        return False
    except Exception as e:
        print(f"Error sending email: {e}")
        print("\nEmail content (manual send required):")
        print("\n" + "="*60)
        print(email_content)
        print("="*60)
        return False

