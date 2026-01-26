"""Pydantic schemas for Agent Builder agent state and data structures."""

from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class AgentIdea(BaseModel):
    """Represents a generated full-stack application idea."""
    
    name: str = Field(..., description="Professional descriptive name (NO 'Smart' prefix)")
    slug: str = Field(..., description="URL-friendly slug (e.g., 'taskflow', 'expense-tracker')")
    description: str = Field(..., description="One-sentence summary of the complete application")
    problem: str = Field(..., description="The substantial problem this full-stack application solves")
    target_audience: str = Field(..., description="Who will use this application")
    category: str = Field(..., description="Category: productivity|finance|health|education|social|commerce|analytics|communication|other")
    tech_stack: Dict[str, str] = Field(default_factory=dict, description="Tech stack with frontend, backend, database, etc.")
    core_features: List[str] = Field(default_factory=list, description="Core features of the application")
    architecture_overview: str = Field(..., description="High-level architecture description")
    date: str = Field(..., description="Date in YYYY-MM-DD format")


class AgentImplementation(BaseModel):
    """Represents the full implementation of a full-stack application."""
    
    idea: AgentIdea
    frontend_files: Dict[str, str] = Field(default_factory=dict, description="Frontend files: path -> content")
    backend_files: Dict[str, str] = Field(default_factory=dict, description="Backend files: path -> content")
    database_files: Dict[str, str] = Field(default_factory=dict, description="Database files: path -> content")
    config_files: Dict[str, str] = Field(default_factory=dict, description="Config files: path -> content")
    pyproject_toml: Optional[str] = Field(None, description="pyproject.toml or package.json content")
    readme_content: str = Field(..., description="README.md content")
    env_example: Optional[str] = Field(None, description=".env.example content if needed")
    docker_compose: Optional[str] = Field(None, description="docker-compose.yml content if applicable")


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
    agent_count: int = Field(default=0, description="Number of applications built so far")


class RegistryEntry(BaseModel):
    """Entry for the registry README."""
    
    date: str
    name: str
    description: str
    category: str
    link: str

