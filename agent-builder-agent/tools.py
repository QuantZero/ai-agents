"""Tools for file operations, git, and email in the Agent Builder."""

import os
import json
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from typing import Optional, Dict, Any
from datetime import datetime

from schemas import AgentIdea, AgentImplementation, RegistryEntry


def get_existing_agents(repo_root: str) -> list[str]:
    """Get list of existing agent names from the ai-built-agents directory at repo root."""
    agents = []
    repo_path = Path(repo_root)
    
    # Check for ai-built-agents/ directory at repo root
    agents_dir = repo_path / "ai-built-agents"
    if agents_dir.exists():
        for item in agents_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                agents.append(item.name)
    
    return agents


def create_agent_directory(repo_root: str, date: str, slug: str) -> str:
    """Create directory for new agent: ai-built-agents/YYYY-MM-DD-agent-name/ at repo root"""
    agents_dir = Path(repo_root) / "ai-built-agents"
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
    """Send email using SMTP (Gmail by default).
    
    Hardcoded recipient: jamesdev0101@gmail.com
    
    Requires SMTP configuration in environment variables:
    - SMTP_SERVER (default: smtp.gmail.com)
    - SMTP_PORT (default: 587)
    - SMTP_USER (Gmail address)
    - SMTP_PASSWORD (Gmail app password)
    """
    # Hardcoded developer email address
    recipient = recipient or "jamesdev0101@gmail.com"
    
    # Parse email content
    lines = email_content.split('\n')
    subject = ""
    body_lines = []
    
    # Extract subject from first line if it starts with "Subject:"
    if lines and lines[0].startswith("Subject:"):
        subject = lines[0].replace("Subject:", "").strip()
        body_lines = lines[1:]
    else:
        # Try to find subject in content
        for i, line in enumerate(lines):
            if line.startswith("Subject:"):
                subject = line.replace("Subject:", "").strip()
                body_lines = lines[i+1:]
                break
        if not subject:
            subject = "Agent Builder Report"
            body_lines = lines
    
    body = '\n'.join(body_lines).strip()
    
    # Get SMTP configuration
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    
    # If SMTP not configured, try system mail, then print
    if not smtp_user or not smtp_password:
        print("\n⚠️  SMTP not configured. Email will not be sent.")
        print("To enable email sending, set SMTP_USER and SMTP_PASSWORD in .env")
        print("\nEmail content:")
        print("\n" + "="*60)
        print(f"To: {recipient}")
        print(f"Subject: {subject}")
        print("-" * 60)
        print(body)
        print("="*60)
        return False
    
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = recipient
        msg['Subject'] = subject
        
        # Add body
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email via SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable encryption
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
        
        print(f"✅ Email sent successfully to {recipient}")
        return True
    
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ SMTP authentication failed: {e}")
        print("Check your SMTP_USER and SMTP_PASSWORD (use Gmail app password)")
        print("\nEmail content (manual send required):")
        print("\n" + "="*60)
        print(f"To: {recipient}")
        print(f"Subject: {subject}")
        print("-" * 60)
        print(body)
        print("="*60)
        return False
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        print("\nEmail content (manual send required):")
        print("\n" + "="*60)
        print(f"To: {recipient}")
        print(f"Subject: {subject}")
        print("-" * 60)
        print(body)
        print("="*60)
        return False

