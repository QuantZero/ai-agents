"""LangGraph workflow for the Agent Builder agent."""

import os
import json
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, END

from schemas import AgentBuilderState, AgentIdea, AgentImplementation
from prompts import (
    SYSTEM_PROMPT,
    IDEA_GENERATION_PROMPT,
    AGENT_IMPLEMENTATION_PROMPT,
    REGISTRY_UPDATE_PROMPT,
    EMAIL_PROMPT,
    ERROR_REPORT_PROMPT,
    SUCCESS_REPORT_PROMPT,
)
from tools import (
    get_existing_agents,
    create_agent_directory,
    write_agent_files,
    update_registry_readme,
    git_commit_and_push,
    send_email,
)

load_dotenv()


class AgentBuilderGraphState(TypedDict):
    """State for the LangGraph workflow."""
    date: str
    existing_agents: list[str]
    idea: dict | None
    implementation: dict | None
    agent_dir: str | None
    registry_readme_path: str
    idea_generated: bool
    implementation_created: bool
    files_written: bool
    registry_updated: bool
    git_committed: bool
    email_sent: bool
    errors: list[str]
    agent_count: int
    registry_content: str


def get_llm():
    """Get the LLM client."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment")
    
    model = os.getenv("OPENAI_MODEL", "gpt-4o")
    return ChatOpenAI(model=model, api_key=api_key, temperature=0.7)


def generate_idea(state: AgentBuilderGraphState) -> AgentBuilderGraphState:
    """Generate a new agent idea."""
    llm = get_llm()
    
    existing_agents_str = ", ".join(state["existing_agents"]) if state["existing_agents"] else "none"
    
    prompt = IDEA_GENERATION_PROMPT.format(
        existing_agents=existing_agents_str
    )
    
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=prompt),
    ]
    
    response = llm.invoke(messages)
    
    # Parse JSON response
    try:
        # Extract JSON from response
        content = response.content
        # Try to find JSON in the response
        if "```json" in content:
            json_start = content.find("```json") + 7
            json_end = content.find("```", json_start)
            json_str = content[json_start:json_end].strip()
        elif "```" in content:
            json_start = content.find("```") + 3
            json_end = content.find("```", json_start)
            json_str = content[json_start:json_end].strip()
        else:
            json_str = content.strip()
        
        idea_dict = json.loads(json_str)
        idea_dict["date"] = state["date"]
        idea = AgentIdea(**idea_dict)
        
        state["idea"] = idea.model_dump()
        state["idea_generated"] = True
        
    except Exception as e:
        state["errors"].append(f"Failed to generate idea: {str(e)}")
        state["idea_generated"] = False
    
    return state


def implement_agent(state: AgentBuilderGraphState) -> AgentBuilderGraphState:
    """Implement the agent based on the idea."""
    if not state.get("idea"):
        state["errors"].append("No idea available for implementation")
        return state
    
    llm = get_llm()
    idea = AgentIdea(**state["idea"])
    
    prompt = AGENT_IMPLEMENTATION_PROMPT.format(
        agent_name=idea.name,
        name=idea.name,
        problem=idea.problem,
        target_audience=idea.target_audience,
        category=idea.category,
        tech_stack=", ".join(idea.tech_stack),
    )
    
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=prompt),
    ]
    
    response = llm.invoke(messages)
    
    # Parse JSON response
    try:
        content = response.content
        # Extract JSON
        if "```json" in content:
            json_start = content.find("```json") + 7
            json_end = content.find("```", json_start)
            json_str = content[json_start:json_end].strip()
        elif "```" in content:
            json_start = content.find("```") + 3
            json_end = content.find("```", json_start)
            json_str = content[json_start:json_end].strip()
        else:
            json_str = content.strip()
        
        impl_dict = json.loads(json_str)
        implementation = AgentImplementation(
            idea=idea,
            **impl_dict
        )
        
        state["implementation"] = implementation.model_dump()
        state["implementation_created"] = True
        
    except Exception as e:
        state["errors"].append(f"Failed to implement agent: {str(e)}")
        state["implementation_created"] = False
    
    return state


def write_files(state: AgentBuilderGraphState) -> AgentBuilderGraphState:
    """Write agent files to disk."""
    if not state.get("implementation"):
        state["errors"].append("No implementation available")
        return state
    
    idea = AgentIdea(**state["idea"])
    implementation = AgentImplementation(**state["implementation"])
    
    # Get repo root (parent of agent-builder-agent)
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Create agent directory
    agent_dir = create_agent_directory(repo_root, state["date"], idea.slug)
    state["agent_dir"] = agent_dir
    
    # Write files
    success = write_agent_files(agent_dir, implementation)
    
    if success:
        state["files_written"] = True
    else:
        state["errors"].append("Failed to write agent files")
        state["files_written"] = False
    
    return state


def update_registry(state: AgentBuilderGraphState) -> AgentBuilderGraphState:
    """Update the registry README."""
    if not state.get("idea") or not state.get("agent_dir"):
        state["errors"].append("Missing idea or agent_dir for registry update")
        return state
    
    idea = AgentIdea(**state["idea"])
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    registry_path = os.path.join(repo_root, state["registry_readme_path"])
    
    # Read current registry
    if os.path.exists(registry_path):
        with open(registry_path, "r") as f:
            registry_content = f.read()
    else:
        registry_content = "# AI Agents Registry\n\n## Available Agents\n\n"
    
    state["registry_content"] = registry_content
    
    # Create registry entry
    entry = {
        "date": state["date"],
        "name": idea.name,
        "description": idea.description,
        "category": idea.category,
        "link": f"./agents/{state['date']}-{idea.slug}/README.md",
    }
    
    # Update registry (simple text manipulation)
    # Find "## Available Agents" section and insert new entry
    lines = registry_content.split('\n')
    new_lines = []
    inserted = False
    in_section = False
    
    for i, line in enumerate(lines):
        if line.startswith('##') and ('Available' in line or 'Agents' in line):
            in_section = True
            new_lines.append(line)
            continue
        
        if in_section and not inserted:
            if line.startswith('###') or (line.startswith('##') and 'Available' not in line):
                # Insert before this entry
                new_lines.append(f"\n### {idea.name}")
                new_lines.append(f"\n{idea.description}")
                new_lines.append(f"\n**Category:** {idea.category}")
                new_lines.append(f"\n**Date:** {state['date']}")
                new_lines.append(f"\n[📖 Read the {idea.name} README]({entry['link']})")
                new_lines.append("")
                inserted = True
        
        new_lines.append(line)
    
    if not inserted:
        # Append to end
        new_lines.append(f"\n### {idea.name}")
        new_lines.append(f"\n{idea.description}")
        new_lines.append(f"\n**Category:** {idea.category}")
        new_lines.append(f"\n**Date:** {state['date']}")
        new_lines.append(f"\n[📖 Read the {idea.name} README]({entry['link']})")
    
    updated_content = '\n'.join(new_lines)
    
    # Write updated registry
    try:
        with open(registry_path, "w") as f:
            f.write(updated_content)
        state["registry_updated"] = True
    except Exception as e:
        state["errors"].append(f"Failed to update registry: {str(e)}")
        state["registry_updated"] = False
    
    return state


def commit_and_push(state: AgentBuilderGraphState) -> AgentBuilderGraphState:
    """Commit and push to GitHub."""
    if not state.get("idea"):
        state["errors"].append("No idea available for git commit")
        return state
    
    idea = AgentIdea(**state["idea"])
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    success, message = git_commit_and_push(repo_root, idea.name, state["date"])
    
    if success:
        state["git_committed"] = True
    else:
        state["errors"].append(f"Git operation failed: {message}")
        state["git_committed"] = False
    
    return state


def send_summary_email(state: AgentBuilderGraphState) -> AgentBuilderGraphState:
    """Send summary email - success report if no errors, error report if errors exist.
    
    Always sends an email to jamesdev0101@gmail.com regardless of success or failure.
    """
    llm = get_llm()
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Check if there are errors or if the run was not fully successful
    has_errors = state.get("errors") and len(state["errors"]) > 0
    is_successful = (
        state.get("idea_generated") and 
        state.get("implementation_created") and 
        state.get("files_written") and 
        state.get("registry_updated")
    )
    
    if has_errors or not is_successful:
        # Send error report
        errors_str = "\n".join([f"- {e}" for e in state["errors"]]) if state.get("errors") else "Unknown error"
        
        # Determine status based on what was completed
        if state.get("files_written"):
            status = "Partial - Files written but registry/git failed"
        elif state.get("implementation_created"):
            status = "Partial - Implementation created but files not written"
        elif state.get("idea_generated"):
            status = "Partial - Idea generated but implementation failed"
        else:
            status = "Failed - Critical error in early stages"
        
        # Include agent info if available
        agent_info = ""
        if state.get("idea"):
            try:
                idea = AgentIdea(**state["idea"])
                agent_info = f"\n\nAgent Info (if created):\n- Name: {idea.name}\n- Description: {idea.description}"
            except:
                pass
        
        prompt = ERROR_REPORT_PROMPT.format(
            date=state["date"],
            errors=errors_str + agent_info,
            status=status,
            agent_count=state["agent_count"],
        )
        
        messages = [
            SystemMessage(content="You are a technical writer. Generate clear, actionable error reports."),
            HumanMessage(content=prompt),
        ]
        
        response = llm.invoke(messages)
        email_content = response.content
        
    else:
        # Send success report
        if not state.get("idea"):
            # This shouldn't happen if successful, but handle it
            errors_str = "No idea available for success report"
            prompt = ERROR_REPORT_PROMPT.format(
                date=state["date"],
                errors=errors_str,
                status="Failed - No idea generated",
                agent_count=state["agent_count"],
            )
            messages = [
                SystemMessage(content="You are a technical writer. Generate clear, actionable error reports."),
                HumanMessage(content=prompt),
            ]
            response = llm.invoke(messages)
            email_content = response.content
        else:
            idea = AgentIdea(**state["idea"])
            github_link = f"{os.getenv('GITHUB_REPO_URL', 'https://github.com/user/repo')}/tree/main/agents/{state['date']}-{idea.slug}"
            
            prompt = SUCCESS_REPORT_PROMPT.format(
                name=idea.name,
                description=idea.description,
                problem=idea.problem,
                category=idea.category,
                tech_stack=", ".join(idea.tech_stack),
                github_link=github_link,
                count=state["agent_count"] + 1,
                date=state["date"],
            )
            
            messages = [
                SystemMessage(content="You are a technical writer. Generate clear, concise success reports."),
                HumanMessage(content=prompt),
            ]
            
            response = llm.invoke(messages)
            email_content = response.content
    
    # Always send email (hardcoded to jamesdev0101@gmail.com)
    success = send_email(email_content)
    
    if success:
        state["email_sent"] = True
    else:
        # Log but don't fail - email is critical for reporting
        state["email_sent"] = False
        state["errors"].append("Email sending failed - manual review required")
    
    return state


def should_continue(state: AgentBuilderGraphState) -> str:
    """Determine if workflow should continue or end."""
    if state.get("errors") and len(state["errors"]) > 0:
        # Check for critical errors
        critical_errors = [e for e in state["errors"] if "idea" in e.lower() or "implementation" in e.lower()]
        if critical_errors:
            return "end"
    
    if state.get("email_sent") or state.get("git_committed"):
        return "end"
    
    return "continue"


def build_graph() -> StateGraph:
    """Build the LangGraph workflow.
    
    The workflow always ends with sending an email report, regardless of success or failure.
    """
    workflow = StateGraph(AgentBuilderGraphState)
    
    # Add nodes
    workflow.add_node("generate_idea", generate_idea)
    workflow.add_node("implement_agent", implement_agent)
    workflow.add_node("write_files", write_files)
    workflow.add_node("update_registry", update_registry)
    workflow.add_node("commit_and_push", commit_and_push)
    workflow.add_node("send_email", send_summary_email)
    
    # Set entry point
    workflow.set_entry_point("generate_idea")
    
    # Add edges - always flow to next step, even if previous step had errors
    # This ensures we always send an email report
    workflow.add_edge("generate_idea", "implement_agent")
    workflow.add_edge("implement_agent", "write_files")
    workflow.add_edge("write_files", "update_registry")
    workflow.add_edge("update_registry", "commit_and_push")
    workflow.add_edge("commit_and_push", "send_email")
    workflow.add_edge("send_email", END)
    
    return workflow.compile()

