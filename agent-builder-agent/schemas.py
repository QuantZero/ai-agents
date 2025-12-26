"""Pydantic schemas for Agent Builder agent state and data structures."""

from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class AgentIdea(BaseModel):
    """Represents a generated agent idea."""
    
    name: str = Field(..., description="Short, descriptive name for the agent")
    slug: str = Field(..., description="URL-friendly slug (e.g., 'code-review-agent')")
    description: str = Field(..., description="One-sentence summary of what the agent does")
    problem: str = Field(..., description="The specific problem this agent solves")
    target_audience: str = Field(..., description="Who this agent is for (developers, founders, etc.)")
    category: str = Field(..., description="Category: dev-tooling, knowledge-management, research, etc.")
    agentic_justification: str = Field(..., description="Why this needs to be an agent vs simple script")
    tech_stack: List[str] = Field(default_factory=list, description="Required technologies")
    date: str = Field(..., description="Date in YYYY-MM-DD format")


class AgentImplementation(BaseModel):
    """Represents the full implementation of an agent."""
    
    idea: AgentIdea
    agent_code: str = Field(..., description="Main agent.py code")
    schemas_code: Optional[str] = Field(None, description="schemas.py code if needed")
    prompts_code: Optional[str] = Field(None, description="prompts.py code if needed")
    graph_code: Optional[str] = Field(None, description="graph.py code if needed")
    tools_code: Optional[str] = Field(None, description="tools.py code if needed")
    pyproject_toml: str = Field(..., description="pyproject.toml content")
    readme_content: str = Field(..., description="README.md content")
    env_example: Optional[str] = Field(None, description=".env.example content if needed")


class AgentBuilderState(BaseModel):
    """State for the agent builder workflow."""
    
    # Input
    date: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    existing_agents: List[str] = Field(default_factory=list, description="List of existing agent names to avoid duplicates")
    
    # Generation
    idea: Optional[AgentIdea] = None
    implementation: Optional[AgentImplementation] = None
    
    # File paths
    agent_dir: Optional[str] = None
    registry_readme_path: str = Field(default="README.md")
    
    # Execution status
    idea_generated: bool = False
    implementation_created: bool = False
    files_written: bool = False
    registry_updated: bool = False
    git_committed: bool = False
    email_sent: bool = False
    
    # Error tracking
    errors: List[str] = Field(default_factory=list)
    
    # Metadata
    agent_count: int = Field(default=0, description="Number of agents built so far")


class RegistryEntry(BaseModel):
    """Entry for the registry README."""
    
    date: str
    name: str
    description: str
    category: str
    link: str

