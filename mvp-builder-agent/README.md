# MVP Builder Agent

An **AI-powered builder agent** that takes a builder prompt from the MVP Planner Agent and generates a **complete, working prototype** with modern tech stacks, best practices, and production-ready code.

## Features

- 🏗️ **Step-by-Step Building**: Breaks down the build into logical phases
- 🎯 **Best Model Available**: Uses GPT-4o (or GPT-4-turbo) for high-quality code generation
- 📐 **Architecture First**: Generates tech stack and architecture before coding
- 💻 **Modern Tech Stacks**: Aware of latest frameworks, libraries, and best practices
- 📁 **Complete Prototypes**: Generates full project structure with all necessary files
- 📝 **Auto-Documentation**: Creates README and setup instructions automatically

## How It Works

The builder agent follows a systematic approach:

1. **Tech Stack & Architecture** (Step 1)
   - Analyzes the builder prompt
   - Recommends appropriate tech stack (frontend, backend, database, etc.)
   - Designs high-level architecture (layers, modules, data flow)
   - Creates project structure

2. **Implementation Plan** (Step 2)
   - Breaks down the build into phases
   - Identifies files to create with dependencies
   - Estimates complexity for each phase

3. **Code Generation** (Step 3)
   - Generates code file by file, phase by phase
   - Respects dependencies between files
   - Uses best practices and modern patterns
   - Creates production-ready, well-documented code

4. **Documentation** (Step 4)
   - Generates comprehensive README
   - Includes setup and running instructions
   - Documents project structure

## Requirements

- Python 3.12+
- `uv` package manager (recommended) or `pip`
- Builder prompt from MVP Planner Agent (or custom prompt)
- **One of the following**:
  - OpenAI API key (`OPENAI_API_KEY`) for OpenAI models
  - Anthropic API key (`ANTHROPIC_API_KEY`) for Claude models
  - Ollama installed locally for local models

## Installation

From the `mvp-builder-agent` directory:

```bash
uv sync
```

Or with `pip`:

```bash
pip install -e .
```

## Configuration

Create a `.env` file in this directory with:

```bash
# Required for OpenAI
OPENAI_API_KEY=your-api-key-here

# Required for Anthropic
ANTHROPIC_API_KEY=your-api-key-here

# Optional: Ollama base URL (defaults to http://localhost:11434)
OLLAMA_BASE_URL=http://localhost:11434

# Optional: Default provider and model
LLM_PROVIDER=openai
LLM_MODEL=gpt-4o

# Optional: Output directory
BUILD_OUTPUT_DIR=generated_prototype
```

### Supported Providers and Models

**OpenAI** (requires `OPENAI_API_KEY`):
- `gpt-5.2-pro` - Latest flagship, best for coding (verify availability)
- `gpt-5.2-thinking` - Complex reasoning and problem-solving (verify availability)
- `gpt-5.2-instant` - Fast and efficient for everyday tasks (verify availability)
- `gpt-4o` - Best overall, excellent for coding (recommended - currently available)
- `gpt-4o-mini` - Faster and cheaper, good for coding
- `gpt-4-turbo` - Previous best model, great for coding
- `gpt-4` - Original GPT-4, solid coding capabilities
- `gpt-3.5-turbo` - Fast and cost-effective

**Anthropic** (requires `ANTHROPIC_API_KEY`):
- `claude-4-5-opus-20251124` - Latest most powerful, best for coding (verify availability)
- `claude-4-5-sonnet-20250929` - Real-world agents, coding, computer use (verify availability)
- `claude-4-5-haiku-20251015` - Lightweight, fast, real-time (verify availability)
- `claude-3-5-sonnet-20241022` - Latest available, best for coding (recommended - currently available)
- `claude-3-5-sonnet-20240620` - Previous version, excellent coding
- `claude-3-opus-20240229` - Most capable, great for complex coding
- `claude-3-sonnet-20240229` - Balanced performance
- `claude-3-haiku-20240307` - Fastest, good for simple coding tasks

**Note:** Claude 4.5 and GPT-5.2 models may not be available yet. If you get errors, use the Claude 3.5 or GPT-4o models which are confirmed available. Verify exact model names with provider documentation.

**Ollama** (requires local Ollama installation):
- `deepseek-coder` - Best coding model for Ollama (recommended)
- `codellama` - Meta's specialized coding model
- `qwen2.5-coder` - Excellent coding capabilities
- `starcoder2` - StarCoder2, coding-focused
- `llama3.2` - Latest Llama, good general coding
- `llama3.1` - Previous Llama version
- `llama3` - Original Llama 3
- `mistral` - Fast and efficient
- `mixtral` - Mixture of experts, powerful
- `deepseek` - General purpose DeepSeek
- `neural-chat` - Good for conversational coding

Note: You only need to set API keys for the providers you plan to use.

## Pricing

### OpenAI Models

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Cached Input (per 1M tokens) |
|-------|----------------------|----------------------|----------------------------|
| GPT-5.2 Pro | $21.00 | $168.00 | N/A |
| GPT-5.2 Thinking | $1.75 | $14.00 | $0.175 |
| GPT-5.2 Instant | $0.25 | $2.00 | $0.025 |
| **GPT-4o** ⭐ | **$2.50** | **$10.00** | **$0.25** |
| GPT-4o-mini | $0.15 | $0.60 | $0.015 |
| GPT-4-turbo | $10.00 | $30.00 | $1.00 |
| GPT-4 | $30.00 | $60.00 | $3.00 |
| GPT-3.5-turbo | $0.50 | $1.50 | $0.05 |

### Anthropic Models

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Cached Input (per 1M tokens) |
|-------|----------------------|----------------------|----------------------------|
| Claude 4.5 Opus | $5.00 | $25.00 | $0.50 |
| Claude 4.5 Sonnet | $3.00 | $15.00 | $0.30 |
| Claude 4.5 Haiku | $1.00 | $5.00 | $0.10 |
| **Claude 3.5 Sonnet** ⭐ | **$3.00** | **$15.00** | **$0.30** |
| Claude 3.5 Sonnet (Jun) | $3.00 | $15.00 | $0.30 |
| Claude 3 Opus | $15.00 | $75.00 | $1.50 |
| Claude 3 Sonnet | $3.00 | $15.00 | $0.30 |
| Claude 3 Haiku | $0.25 | $1.25 | $0.025 |

### Ollama Models

| Model | Cost |
|-------|------|
| All Ollama Models | **🆓 Free** (runs locally on your machine) |

**Notes:**
- ⭐ = Recommended models for best coding quality
- Cached input pricing applies when using prompt caching (90% discount for repeated prompts)
- Ollama models are completely free but require local installation and hardware resources
- Pricing is per million tokens (1M tokens ≈ 750,000 words)
- Prices are subject to change - check official provider documentation for latest pricing

**Cost Estimation Example:**
- Building a medium prototype (~50K input tokens, ~20K output tokens):
  - GPT-4o: ~$0.33
  - Claude 3.5 Sonnet: ~$0.45
  - Ollama: $0.00 (free)

## Usage

### Web UI (Recommended)

Launch the interactive web interface:

```bash
uv run streamlit run ui.py
```

The UI provides:
- 📤 **Upload builder prompt** from MVP Planner Agent
- 📝 **Paste prompt directly** or load from file
- 🤖 **Select LLM provider and model** (OpenAI, Anthropic, or Ollama)
- 🔨 **Watch step-by-step building** in real-time
- 📁 **Download generated prototype** as zip
- 📊 **View architecture and implementation plan**

### CLI Mode

Run the command-line interface:

```bash
uv run python main.py
```

You'll be prompted to:
1. Provide the builder prompt (file path or paste directly)
2. Specify output directory (optional)

The agent will use the default provider/model from `.env` (or OpenAI gpt-4o if not set).

To use a different provider/model, set environment variables:
```bash
LLM_PROVIDER=anthropic LLM_MODEL=claude-3-5-sonnet-20241022 uv run python main.py
```

The agent will then:
- Generate tech stack and architecture
- Create implementation plan
- Build files phase by phase
- Generate README and documentation

### Programmatic Usage

```python
from main import build_prototype, load_builder_prompt

# Load builder prompt
prompt = load_builder_prompt("builder_prompt.txt")

# Build prototype with default model (OpenAI gpt-4o)
output_path = build_prototype(prompt, output_dir="my_prototype")

# Or specify provider and model
output_path = build_prototype(
    prompt,
    output_dir="my_prototype",
    provider="anthropic",
    model="claude-3-5-sonnet-20241022"
)

# Or use Ollama for local generation
output_path = build_prototype(
    prompt,
    output_dir="my_prototype",
    provider="ollama",
    model="llama3.2"
)

print(f"Prototype created at: {output_path}")
```

## Output Structure

The generated prototype includes:

```
generated_prototype/
├── architecture.json          # Tech stack and architecture plan
├── implementation_plan.json   # Detailed implementation phases
├── README.md                  # Setup and usage instructions
├── [project files]            # Generated code files
└── ...
```

## Integration with MVP Planner Agent

1. **Generate builder prompt** using MVP Planner Agent:
   ```bash
   cd ../mvp-planner-agent
   uv run streamlit run ui.py
   # Follow the flow to get builder_prompt.txt
   ```

2. **Build prototype** using Builder Agent:
   ```bash
   cd ../mvp-builder-agent
   uv run streamlit run ui.py
   # Upload builder_prompt.txt and build!
   ```

## Tech Stack Awareness

The builder agent is aware of modern technologies including:

- **Frontend**: React, Vue, Angular, Next.js, Svelte, SwiftUI, Flutter, React Native
- **Backend**: Node.js, Python (FastAPI, Django), Go, Rust, Java (Spring)
- **Databases**: PostgreSQL, MongoDB, SQLite, Redis, Supabase, Firebase
- **Deployment**: Docker, Vercel, AWS, GCP, Railway, Render
- **Best Practices**: Clean architecture, SOLID principles, testing, CI/CD

## Example Workflow

1. **Plan** with MVP Planner Agent → Get `builder_prompt.txt`
2. **Build** with Builder Agent → Get `generated_prototype/`
3. **Review** generated code and architecture
4. **Customize** as needed
5. **Deploy** your prototype!

## Project Structure

```text
mvp-builder-agent/
├── main.py           # Core builder logic
├── ui.py             # Streamlit web UI
├── pyproject.toml    # Dependencies
├── README.md         # This file
└── .env              # Configuration (gitignored)
```

## Notes

- The builder supports **multiple LLM providers**: OpenAI, Anthropic, and Ollama
- Default model is **GPT-4o** (OpenAI) for best code quality
- You can choose any supported model in the UI or via code
- **Ollama** allows completely local generation (no API costs)
- Generated code follows **modern best practices** and design patterns
- Files are generated **step-by-step** respecting dependencies
- The prototype is **ready to run** after generation (may need dependency installation)
- Architecture and implementation plans are saved as JSON for review

## Troubleshooting

- **JSON parsing errors**: The model might return markdown-wrapped JSON. The agent handles this automatically.
- **Missing dependencies**: Some generated code may require additional packages. Check the README for setup instructions.
- **Large prompts**: For very complex applications, the build may take time. Progress is shown in real-time.

## Next Steps

After generating a prototype:
1. Review the architecture and implementation plan
2. Install dependencies as specified in README
3. Test the generated code
4. Customize and extend as needed
5. Deploy when ready!

