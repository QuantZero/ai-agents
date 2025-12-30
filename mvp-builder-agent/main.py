import os
import json
from pathlib import Path
from typing import Dict, List, Optional, Literal
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.language_models import BaseChatModel

load_dotenv(override=True)

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# Default settings
DEFAULT_PROVIDER = os.getenv("LLM_PROVIDER", "openai")
DEFAULT_MODEL = os.getenv("LLM_MODEL", "gpt-4o")
BUILD_OUTPUT_DIR = os.getenv("BUILD_OUTPUT_DIR", "generated_prototype")

# Pricing information per million tokens (as of December 2024)
# Format: {model_name: {"input": price, "output": price, "cached_input": price or None}}
MODEL_PRICING = {
    # OpenAI Models
    "gpt-5.2-pro": {"input": 21.00, "output": 168.00, "cached_input": None},
    "gpt-5.2-thinking": {"input": 1.75, "output": 14.00, "cached_input": 0.175},
    "gpt-5.2-instant": {"input": 0.25, "output": 2.00, "cached_input": 0.025},
    "gpt-4o": {"input": 2.50, "output": 10.00, "cached_input": 0.25},
    "gpt-4o-mini": {"input": 0.15, "output": 0.60, "cached_input": 0.015},
    "gpt-4-turbo": {"input": 10.00, "output": 30.00, "cached_input": 1.00},
    "gpt-4": {"input": 30.00, "output": 60.00, "cached_input": 3.00},
    "gpt-3.5-turbo": {"input": 0.50, "output": 1.50, "cached_input": 0.05},
    
    # Anthropic Models
    "claude-4-5-opus-20251124": {"input": 5.00, "output": 25.00, "cached_input": 0.50},
    "claude-4-5-sonnet-20250929": {"input": 3.00, "output": 15.00, "cached_input": 0.30},
    "claude-4-5-haiku-20251015": {"input": 1.00, "output": 5.00, "cached_input": 0.10},
    "claude-3-5-sonnet-20241022": {"input": 3.00, "output": 15.00, "cached_input": 0.30},
    "claude-3-5-sonnet-20240620": {"input": 3.00, "output": 15.00, "cached_input": 0.30},
    "claude-3-opus-20240229": {"input": 15.00, "output": 75.00, "cached_input": 1.50},
    "claude-3-sonnet-20240229": {"input": 3.00, "output": 15.00, "cached_input": 0.30},
    "claude-3-haiku-20240307": {"input": 0.25, "output": 1.25, "cached_input": 0.025},
    
    # Ollama Models (Free - runs locally)
    "deepseek-coder": {"input": 0.00, "output": 0.00, "cached_input": None, "note": "Free - runs locally"},
    "codellama": {"input": 0.00, "output": 0.00, "cached_input": None, "note": "Free - runs locally"},
    "qwen2.5-coder": {"input": 0.00, "output": 0.00, "cached_input": None, "note": "Free - runs locally"},
    "starcoder2": {"input": 0.00, "output": 0.00, "cached_input": None, "note": "Free - runs locally"},
    "llama3.2": {"input": 0.00, "output": 0.00, "cached_input": None, "note": "Free - runs locally"},
    "llama3.1": {"input": 0.00, "output": 0.00, "cached_input": None, "note": "Free - runs locally"},
    "llama3": {"input": 0.00, "output": 0.00, "cached_input": None, "note": "Free - runs locally"},
    "mistral": {"input": 0.00, "output": 0.00, "cached_input": None, "note": "Free - runs locally"},
    "mixtral": {"input": 0.00, "output": 0.00, "cached_input": None, "note": "Free - runs locally"},
    "deepseek": {"input": 0.00, "output": 0.00, "cached_input": None, "note": "Free - runs locally"},
    "neural-chat": {"input": 0.00, "output": 0.00, "cached_input": None, "note": "Free - runs locally"},
}

# Available models by provider (updated with latest best coding models)
AVAILABLE_MODELS = {
    "openai": [
        "GPT-5.2-codex",
        "gpt-5.2-pro",         # Latest flagship, best for coding (if available)
        "gpt-5.2-thinking",    # Complex reasoning and problem-solving
        "gpt-5.2-instant",     # Fast and efficient for everyday tasks
        "gpt-4o",              # Best overall, excellent for coding (recommended - currently available)
        "gpt-4o-mini",         # Faster and cheaper, good for coding
        "gpt-4-turbo",         # Previous best model, great for coding
        "gpt-4",               # Original GPT-4, solid coding capabilities
        "gpt-3.5-turbo",       # Fast and cost-effective
    ],
    "anthropic": [
        "claude-4-5-opus-20251124",   # Latest most powerful, best for coding (if available)
        "claude-4-5-sonnet-20250929", # Real-world agents, coding, computer use (if available)
        "claude-4-5-haiku-20251015",  # Lightweight, fast, real-time (if available)
        "claude-3-5-sonnet-20241022",  # Latest available, best for coding (recommended - currently available)
        "claude-3-5-sonnet-20240620",  # Previous version, excellent coding
        "claude-3-opus-20240229",      # Most capable, great for complex coding
        "claude-3-sonnet-20240229",    # Balanced performance
        "claude-3-haiku-20240307",     # Fastest, good for simple coding tasks
    ],
    "ollama": [
        "deepseek-coder",      # Best coding model for Ollama (recommended)
        "codellama",           # Meta's specialized coding model
        "qwen2.5-coder",      # Excellent coding capabilities
        "starcoder2",          # StarCoder2, coding-focused
        "llama3.2",            # Latest Llama, good general coding
        "llama3.1",            # Previous Llama version
        "llama3",              # Original Llama 3
        "mistral",             # Fast and efficient
        "mixtral",             # Mixture of experts, powerful
        "deepseek",            # General purpose DeepSeek
        "neural-chat",         # Good for conversational coding
    ],
}


def create_llm(
    provider: Literal["openai", "anthropic", "ollama"] = DEFAULT_PROVIDER,
    model: str = DEFAULT_MODEL,
    temperature: float = 0.1,
) -> BaseChatModel:
    """
    Factory function to create an LLM instance from the specified provider.
    
    Args:
        provider: One of "openai", "anthropic", or "ollama"
        model: Model name for the provider
        temperature: Temperature for generation (default 0.1 for consistent code)
    
    Returns:
        BaseChatModel instance
    """
    if provider == "openai":
        if not OPENAI_API_KEY:
            raise RuntimeError(
                "OPENAI_API_KEY is not set. Add it to a .env file in mvp-builder-agent/."
            )
        return ChatOpenAI(
            model=model,
            temperature=temperature,
            api_key=OPENAI_API_KEY,
        )
    
    elif provider == "anthropic":
        try:
            from langchain_anthropic import ChatAnthropic
        except ImportError:
            raise RuntimeError(
                "langchain-anthropic is not installed. Run: uv sync"
            )
        
        if not ANTHROPIC_API_KEY:
            raise RuntimeError(
                "ANTHROPIC_API_KEY is not set. Add it to a .env file in mvp-builder-agent/."
            )
        return ChatAnthropic(
            model=model,
            temperature=temperature,
            api_key=ANTHROPIC_API_KEY,
        )
    
    elif provider == "ollama":
        try:
            from langchain_ollama import ChatOllama
        except ImportError:
            raise RuntimeError(
                "langchain-ollama is not installed. Run: uv sync"
            )
        
        return ChatOllama(
            model=model,
            temperature=temperature,
            base_url=OLLAMA_BASE_URL,
        )
    
    else:
        raise ValueError(f"Unknown provider: {provider}. Must be one of: openai, anthropic, ollama")


# Global LLM instance (lazy initialization)
_llm: Optional[BaseChatModel] = None
_provider: str = DEFAULT_PROVIDER
_model: str = DEFAULT_MODEL


def get_llm(
    provider: Optional[Literal["openai", "anthropic", "ollama"]] = None,
    model: Optional[str] = None,
) -> BaseChatModel:
    """
    Get or initialize the LLM instance.
    If provider/model are provided, creates a new instance.
    Otherwise, uses cached instance or creates with defaults.
    """
    global _llm, _provider, _model
    
    # If provider/model specified, create new instance
    if provider is not None or model is not None:
        provider = provider or _provider or DEFAULT_PROVIDER
        model = model or _model or DEFAULT_MODEL
        return create_llm(provider, model)
    
    # Otherwise, use cached instance or create with defaults
    if _llm is None:
        _provider = DEFAULT_PROVIDER
        _model = DEFAULT_MODEL
        _llm = create_llm(_provider, _model)
    
    return _llm


def get_model_pricing(model_name: str) -> Optional[Dict]:
    """
    Get pricing information for a specific model.
    
    Args:
        model_name: Name of the model
        
    Returns:
        Dictionary with pricing info or None if not found
    """
    return MODEL_PRICING.get(model_name)


def format_pricing_info(model_name: str) -> str:
    """
    Format pricing information as a readable string.
    
    Args:
        model_name: Name of the model
        
    Returns:
        Formatted pricing string
    """
    pricing = get_model_pricing(model_name)
    if not pricing:
        return "Pricing information not available"
    
    if pricing.get("note") == "Free - runs locally":
        return "🆓 Free (runs locally)"
    
    input_price = pricing.get("input", 0)
    output_price = pricing.get("output", 0)
    cached = pricing.get("cached_input")
    
    result = f"Input: ${input_price:.2f}/1M tokens | Output: ${output_price:.2f}/1M tokens"
    if cached is not None:
        result += f" | Cached: ${cached:.3f}/1M tokens"
    
    return result


def load_builder_prompt(prompt_path: str) -> str:
    """Load builder prompt from file"""
    try:
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except OSError as e:
        raise RuntimeError(f"Failed to read builder prompt from '{prompt_path}': {e}")


def create_project_structure(base_dir: Path, structure: Dict) -> None:
    """Create directory structure for the project"""
    for item, content in structure.items():
        item_path = base_dir / item
        if isinstance(content, dict):
            # It's a directory
            item_path.mkdir(parents=True, exist_ok=True)
            create_project_structure(item_path, content)
        else:
            # It's a file
            item_path.parent.mkdir(parents=True, exist_ok=True)
            item_path.write_text(content, encoding="utf-8")


def generate_tech_stack_and_architecture(
    builder_prompt: str,
    llm: Optional[BaseChatModel] = None,
) -> Dict:
    """
    Step 1: Generate tech stack choice and high-level architecture
    """
    system_prompt = """You are an expert software architect specializing in modern application development.
You excel at choosing the right tech stack and designing scalable, maintainable architectures.

Your task is to analyze the builder prompt and generate:
1. A recommended tech stack with justification
2. High-level architecture (layers, modules, data flow)
3. Project structure (directories and key files)

Respond in JSON format with this structure:
{
    "tech_stack": {
        "frontend": "...",
        "backend": "...",
        "database": "...",
        "deployment": "...",
        "justification": "..."
    },
    "architecture": {
        "layers": ["...", "..."],
        "modules": ["...", "..."],
        "data_flow": "..."
    },
    "project_structure": {
        "directory_name": {
            "file_name": "file content or null for directories"
        }
    }
}"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Builder Prompt:\n\n{builder_prompt}\n\nGenerate the tech stack and architecture plan.")
    ]
    
    llm_instance = llm or get_llm()
    response = llm_instance.invoke(messages)
    try:
        # Extract JSON from response
        content = response.content
        # Try to find JSON block
        if "```json" in content:
            json_start = content.find("```json") + 7
            json_end = content.find("```", json_start)
            content = content[json_start:json_end].strip()
        elif "```" in content:
            json_start = content.find("```") + 3
            json_end = content.find("```", json_start)
            content = content[json_start:json_end].strip()
        
        return json.loads(content)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Failed to parse architecture JSON: {e}\nResponse was: {response.content}")


def generate_implementation_plan(
    builder_prompt: str,
    architecture: Dict,
    llm: Optional[BaseChatModel] = None,
) -> List[Dict]:
    """
    Step 2: Generate a detailed implementation plan with phases
    """
    system_prompt = """You are an expert software engineer who creates detailed, actionable implementation plans.

Given a builder prompt and architecture, create a step-by-step implementation plan.

Respond in JSON format with this structure:
{
    "phases": [
        {
            "phase_number": 1,
            "name": "Phase name",
            "description": "What this phase accomplishes",
            "files_to_create": [
                {
                    "path": "relative/path/to/file.ext",
                    "purpose": "What this file does",
                    "dependencies": ["other files this depends on"]
                }
            ],
            "estimated_complexity": "low|medium|high"
        }
    ]
}"""

    architecture_str = json.dumps(architecture, indent=2)
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Builder Prompt:\n\n{builder_prompt}\n\nArchitecture:\n\n{architecture_str}\n\nGenerate the implementation plan.")
    ]
    
    llm_instance = llm or get_llm()
    response = llm_instance.invoke(messages)
    try:
        content = response.content
        if "```json" in content:
            json_start = content.find("```json") + 7
            json_end = content.find("```", json_start)
            content = content[json_start:json_end].strip()
        elif "```" in content:
            json_start = content.find("```") + 3
            json_end = content.find("```", json_start)
            content = content[json_start:json_end].strip()
        
        plan = json.loads(content)
        return plan.get("phases", [])
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Failed to parse implementation plan JSON: {e}\nResponse was: {response.content}")


def generate_file_content(
    builder_prompt: str,
    architecture: Dict,
    file_path: str,
    file_purpose: str,
    dependencies: List[str],
    existing_files: Dict[str, str],
    llm: Optional[BaseChatModel] = None,
) -> str:
    """
    Step 3: Generate actual code for a specific file
    """
    system_prompt = """You are an expert software engineer writing production-quality code.

You excel at:
- Writing clean, maintainable, well-documented code
- Following modern best practices and design patterns
- Using appropriate frameworks and libraries
- Creating modular, testable code
- Following language-specific conventions and style guides

Generate complete, runnable code for the requested file. Include:
- Proper imports and dependencies
- Clear documentation and comments
- Error handling where appropriate
- Type hints (if applicable)
- Best practices for the chosen tech stack

Return ONLY the code, no explanations or markdown formatting."""

    architecture_str = json.dumps(architecture, indent=2)
    dependencies_info = "\n".join([f"- {dep}: {existing_files.get(dep, 'Not yet created')[:200]}..." 
                                   for dep in dependencies if dep in existing_files])
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"""Builder Prompt:
{builder_prompt}

Architecture:
{architecture_str}

File to generate:
- Path: {file_path}
- Purpose: {file_purpose}
- Dependencies: {', '.join(dependencies) if dependencies else 'None'}

Existing files (for reference):
{dependencies_info if dependencies_info else "No dependencies yet"}

Generate the complete code for {file_path}:""")
    ]
    
    llm_instance = llm or get_llm()
    response = llm_instance.invoke(messages)
    content = response.content
    
    # Clean up markdown code blocks if present
    if "```" in content:
        lines = content.split("\n")
        # Remove first ``` line and language tag
        if lines[0].strip().startswith("```"):
            lines = lines[1:]
        # Remove last ``` line
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        content = "\n".join(lines)
    
    return content.strip()


def build_prototype(
    builder_prompt: str,
    output_dir: str = BUILD_OUTPUT_DIR,
    provider: Optional[Literal["openai", "anthropic", "ollama"]] = None,
    model: Optional[str] = None,
) -> Path:
    """
    Main function: Build the prototype step by step
    
    Args:
        builder_prompt: The builder prompt from MVP Planner Agent
        output_dir: Directory to output the prototype
        provider: LLM provider ("openai", "anthropic", or "ollama")
        model: Model name for the provider
    """
    # Initialize LLM with specified provider/model
    llm_instance = get_llm(provider, model)
    provider_name = provider or DEFAULT_PROVIDER
    model_name = model or DEFAULT_MODEL
    
    print(f"\n{'='*60}")
    print("🚀 MVP Builder Agent - Step-by-Step Prototype Generation")
    print(f"🤖 Using: {provider_name.upper()} - {model_name}")
    print(f"{'='*60}\n")
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Step 1: Generate tech stack and architecture
    print("📐 Step 1: Generating tech stack and architecture...")
    architecture = generate_tech_stack_and_architecture(builder_prompt, llm_instance)
    print(f"✅ Tech Stack: {architecture['tech_stack'].get('frontend', 'N/A')} + {architecture['tech_stack'].get('backend', 'N/A')}")
    
    # Save architecture plan
    arch_file = output_path / "architecture.json"
    arch_file.write_text(json.dumps(architecture, indent=2), encoding="utf-8")
    print(f"💾 Architecture saved to: {arch_file}\n")
    
    # Step 2: Generate implementation plan
    print("📋 Step 2: Generating implementation plan...")
    phases = generate_implementation_plan(builder_prompt, architecture, llm_instance)
    print(f"✅ Created {len(phases)} implementation phases\n")
    
    # Save implementation plan
    plan_file = output_path / "implementation_plan.json"
    plan_file.write_text(json.dumps({"phases": phases}, indent=2), encoding="utf-8")
    print(f"💾 Implementation plan saved to: {plan_file}\n")
    
    # Step 3: Generate files phase by phase
    existing_files = {}
    total_files = sum(len(phase.get("files_to_create", [])) for phase in phases)
    current_file = 0
    
    for phase in phases:
        phase_num = phase.get("phase_number", 0)
        phase_name = phase.get("name", f"Phase {phase_num}")
        files_to_create = phase.get("files_to_create", [])
        
        print(f"{'='*60}")
        print(f"🔨 Phase {phase_num}: {phase_name}")
        print(f"   {phase.get('description', '')}")
        print(f"{'='*60}\n")
        
        for file_info in files_to_create:
            current_file += 1
            file_path = file_info.get("path", "")
            file_purpose = file_info.get("purpose", "")
            dependencies = file_info.get("dependencies", [])
            
            if not file_path:
                continue
            
            print(f"[{current_file}/{total_files}] Generating: {file_path}")
            
            try:
                content = generate_file_content(
                    builder_prompt,
                    architecture,
                    file_path,
                    file_purpose,
                    dependencies,
                    existing_files,
                    llm_instance,
                )
                
                # Write file
                full_path = output_path / file_path
                full_path.parent.mkdir(parents=True, exist_ok=True)
                full_path.write_text(content, encoding="utf-8")
                
                # Store for future dependencies
                existing_files[file_path] = content
                print(f"   ✅ Created: {full_path}\n")
                
            except Exception as e:
                print(f"   ❌ Error generating {file_path}: {e}\n")
                # Continue with other files
                continue
    
    # Step 4: Generate README and setup instructions
    print(f"{'='*60}")
    print("📝 Step 4: Generating README and setup instructions...")
    print(f"{'='*60}\n")
    
    readme_content = generate_readme(builder_prompt, architecture, phases, llm_instance)
    readme_path = output_path / "README.md"
    readme_path.write_text(readme_content, encoding="utf-8")
    print(f"✅ README created: {readme_path}\n")
    
    print(f"{'='*60}")
    print(f"🎉 Prototype generation complete!")
    print(f"📁 Output directory: {output_path.absolute()}")
    print(f"📊 Total files created: {len(existing_files)}")
    print(f"{'='*60}\n")
    
    return output_path


def generate_readme(
    builder_prompt: str,
    architecture: Dict,
    phases: List[Dict],
    llm: Optional[BaseChatModel] = None,
) -> str:
    """Generate a comprehensive README for the prototype"""
    system_prompt = """You are a technical writer creating clear, comprehensive README files for software projects.

Create a README that includes:
- Project description
- Tech stack overview
- Setup instructions
- Running the application
- Project structure
- Next steps

Make it professional and easy to follow."""

    architecture_str = json.dumps(architecture, indent=2)
    phases_str = json.dumps(phases, indent=2)
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"""Builder Prompt:
{builder_prompt}

Architecture:
{architecture_str}

Implementation Phases:
{phases_str}

Generate a comprehensive README.md file:""")
    ]
    
    llm_instance = llm or get_llm()
    response = llm_instance.invoke(messages)
    content = response.content
    
    # Clean up markdown formatting if needed
    if content.startswith("```markdown"):
        content = content[11:]
    if content.startswith("```"):
        content = content[3:]
    if content.endswith("```"):
        content = content[:-3]
    
    return content.strip()


def main() -> None:
    """CLI entry point"""
    print("\n=== MVP Builder Agent ===")
    print("This agent builds a working prototype from a builder prompt.\n")
    
    prompt_source = input(
        "Enter path to builder prompt file (or paste prompt, type 'paste'): "
    ).strip()
    
    if prompt_source.lower() == "paste":
        print("\nPaste the builder prompt (end with empty line + Ctrl+D or Ctrl+Z):")
        lines = []
        try:
            while True:
                line = input()
                lines.append(line)
        except EOFError:
            pass
        builder_prompt = "\n".join(lines).strip()
    else:
        builder_prompt = load_builder_prompt(prompt_source)
    
    if not builder_prompt:
        print("No builder prompt provided. Exiting.")
        return
    
    output_dir = input(
        f"Output directory (default: {BUILD_OUTPUT_DIR}): "
    ).strip() or BUILD_OUTPUT_DIR
    
    try:
        build_prototype(builder_prompt, output_dir)
    except Exception as e:
        print(f"\n❌ Error building prototype: {e}")
        raise


if __name__ == "__main__":
    main()

