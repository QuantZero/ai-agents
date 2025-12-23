## Overview

This repository contains independent AI agent projects, each with its own purpose and dependencies. All agents are designed to be simple, focused, and easy to use. It is basically a collection of small, focused AI agents built with Python. Each agent is designed to solve a specific task using modern AI/LLM technologies. 

> Multi agent flows will be added soon

## Available Agents

### 🚀 MVP Planner Agent

A planning agent that helps refine mobile app MVP ideas into clear, technical, builder-ready specifications. Generates a comprehensive builder prompt for the MVP Builder Agent.

**Features:**
- Asks focused clarifying questions
- Generates structured MVP + technical requirements spec
- Outputs builder-ready prompt
- Interactive web UI and CLI

**Tech Stack:** LangChain, OpenAI API, Streamlit

[📖 Read the MVP Planner Agent README](./mvp-planner-agent/README.md)

### 🔨 MVP Builder Agent

An AI-powered builder that takes builder prompts and generates complete, working prototypes with modern tech stacks, best practices, and production-ready code.

**Features:**
- Step-by-step building process
- Uses GPT-4o for high-quality code generation
- Generates architecture and implementation plans
- Creates complete project structures
- Auto-generates documentation

**Tech Stack:** LangChain, OpenAI API, Streamlit

[📖 Read the MVP Builder Agent README](./mvp-builder-agent/README.md)

### 📧 Email Agent

A local LLM agent that connects to your IMAP inbox, lists unread emails, and provides intelligent summaries. Built with LangGraph and LangChain, running against a local Ollama model.

**Features:**
- Lists the most recent unread email
- Summarizes emails by IMAP UID
- Interactive CLI interface
- Runs entirely locally (no cloud API required)

**Tech Stack:** LangGraph, LangChain, Ollama, IMAP

[📖 Read the Email Agent README](./email-agent/README.md)

### 🌐 Scraper Agent

A web scraping tool that uses OpenAI's GPT-4o-mini to generate intelligent, readable summaries of any website. Perfect for quickly understanding what a website is about without wading through navigation menus and clutter.

**Features:**
- Smart URL handling (accepts URLs in any format)
- Content extraction (filters out navigation, headers, scripts)
- AI-powered summaries with a touch of wit
- Terminal-friendly output

**Tech Stack:** OpenAI API, BeautifulSoup, Requests

[📖 Read the Scraper Agent README](./scraper-agent/README.md)

## Getting Started

Each agent is independent and can be set up separately. Navigate to the agent's directory and follow its specific README for detailed setup instructions.

### Prerequisites

- **Python 3.12+** (Python 3.13+ for email-agent)
- **uv** package manager (recommended) or pip
- Agent-specific requirements:
  - **MVP Planner Agent**: OpenAI API key
  - **MVP Builder Agent**: OpenAI API key (GPT-4o recommended)
  - **Email Agent**: Ollama running locally with a compatible model
  - **Scraper Agent**: OpenAI API key

### Quick Setup

1. **Clone or navigate to this repository:**
   ```bash
   cd ai-projects
   ```

2. **Choose an agent and navigate to its directory:**
   ```bash
   cd mvp-planner-agent    # or mvp-builder-agent, email-agent, scraper-agent
   ```

3. **Install dependencies:**
   ```bash
   uv sync
   ```
   Or with pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Create a `.env` file in the agent's directory
   - Add the required configuration (see each agent's README)

5. **Run the agent:**
   ```bash
   python main.py
   ```

## Project Structure

```
ai-agents/
├── mvp-planner-agent/    # MVP planning agent
│   ├── main.py           # Main entry point
│   ├── ui.py             # Streamlit web UI
│   ├── pyproject.toml    # Dependencies
│   ├── README.md         # Detailed documentation
│   └── .env              # Configuration (gitignored)
│
├── mvp-builder-agent/    # MVP builder agent
│   ├── main.py           # Main entry point
│   ├── ui.py             # Streamlit web UI
│   ├── pyproject.toml    # Dependencies
│   ├── README.md         # Detailed documentation
│   └── .env              # Configuration (gitignored)
│
├── email-agent/          # Email management agent
│   ├── main.py           # Main entry point
│   ├── pyproject.toml   # Dependencies
│   ├── README.md         # Detailed documentation
│   └── .env              # Configuration (gitignored)
│
├── scraper-agent/        # Web scraping agent
│   ├── main.py           # Main entry point
│   ├── scraper.py        # Scraping utilities
│   ├── pyproject.toml    # Dependencies
│   ├── README.md         # Detailed documentation
│   └── .env              # Configuration (gitignored)
│
└── README.md             # This file
```

## Common Patterns

All agents in this repository follow similar patterns:

- **Configuration**: Environment variables via `.env` files
- **Dependencies**: Managed with `pyproject.toml` and `uv`
- **CLI Interface**: Simple, interactive command-line interfaces
- **Error Handling**: Clear error messages and debugging information
- **Documentation**: Each agent has its own comprehensive README

## Adding New Agents

When adding a new agent to this repository:

1. Create a new directory with a descriptive name (e.g., `new-agent/`)
2. Include a `README.md` with:
   - Description and features
   - Installation instructions
   - Configuration requirements
   - Usage examples
3. Use `pyproject.toml` for dependency management
4. Add a `.env.example` file if environment variables are needed
5. Follow the existing code structure and patterns

## Contributing

Each agent is designed to be independent and self-contained. Feel free to:
- Improve existing agents
- Add new agents
- Fix bugs
- Enhance documentation

## License

Each agent may have its own license. Check individual agent directories for license information.

## Notes

- All `.env` files are gitignored for security
- Each agent can be used independently
- Agents are designed to be simple and focused on a single task
- Local models (like Ollama) are preferred where possible to reduce API costs

