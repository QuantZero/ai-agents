## Overview

This repository contains independent AI agent projects, each with its own purpose and dependencies. All agents are designed to be simple, focused, and easy to use. It is basically a collection of small, focused AI agents built with Python. Each agent is designed to solve a specific task using modern AI/LLM technologies.

**New AI generated agents are automatically built daily** by the [Agent Builder Agent](./agent-builder-agent/README.md) and added to the [`ai-built-agents`](./ai-built-agents/) directory.

> Multi agent flows will be added soon

## Available Agents

### AI-Built Agents

See the [ai-built-agents README](./ai-built-agents/README.md) for the complete list.

### Human-Built Agents

[📖 Read the Dependency Conflict Resolver README](./ai-built-agents/2025-12-26-dependency-conflict-resolver/README.md)














### Smart Home Maintenance Scheduler

Effortlessly manage and schedule home maintenance tasks to keep your living space in top condition.

**Category:** lifestyle

**Date:** 2026-01-10

[📖 Read the Smart Home Maintenance Scheduler README](./ai-built-agents/2026-01-10-smart-home-maintenance-scheduler/README.md)

### Smart Job Application Tracker

Streamline your job search with a dynamic agent that organizes, tracks, and optimizes your application process.

**Category:** career

**Date:** 2026-01-09

[📖 Read the Smart Job Application Tracker README](./ai-built-agents/2026-01-09-smart-job-application-tracker/README.md)

### Smart Sleep Quality Enhancer

An AI agent that optimizes your sleep environment and routines for better rest and recovery.

**Category:** health

**Date:** 2026-01-07

[📖 Read the Smart Sleep Quality Enhancer README](./ai-built-agents/2026-01-07-smart-sleep-quality-enhancer/README.md)

### Smart Daily Commute Optimizer

Optimizes daily commute by providing real-time updates and alternative routes to save time and reduce stress.

**Category:** productivity

**Date:** 2026-01-06

[📖 Read the Smart Daily Commute Optimizer README](./ai-built-agents/2026-01-06-smart-daily-commute-optimizer/README.md)

### Smart Daily Meal Optimizer

Effortlessly plan nutritious and budget-friendly meals tailored to your dietary needs and preferences.

**Category:** lifestyle

**Date:** 2026-01-05

[📖 Read the Smart Daily Meal Optimizer README](./ai-built-agents/2026-01-05-smart-daily-meal-optimizer/README.md)

### Smart Social Scheduler

Seamlessly organizes social gatherings, making it easy for everyday people to connect and maintain relationships.

**Category:** communication

**Date:** 2026-01-03

[📖 Read the Smart Social Scheduler README](./ai-built-agents/2026-01-03-smart-social-scheduler/README.md)

### Smart Career Pathfinder

Guides individuals in identifying and pursuing optimal career paths based on skills, interests, and market trends.

**Category:** career

**Date:** 2026-01-02

[📖 Read the Smart Career Pathfinder README](./ai-built-agents/2026-01-02-smart-career-pathfinder/README.md)

### Smart Home Security Advisor

An AI agent that proactively advises homeowners to enhance their home security, reducing risks of burglaries and intrusions.

**Category:** safety

**Date:** 2025-12-31

[📖 Read the Smart Home Security Advisor README](./ai-built-agents/2025-12-31-smart-home-security-advisor/README.md)

### Smart Grocery Saver

Optimizes grocery shopping and budgeting to reduce waste and save money for everyday families.

**Category:** lifestyle

**Date:** 2025-12-30

[📖 Read the Smart Grocery Saver README](./ai-built-agents/2025-12-30-smart-grocery-saver/README.md)

### Smart Daily Energy Manager

A personalized agent that optimizes daily energy levels by recommending activities and rest periods to enhance productivity and well-being.

**Category:** wellbeing

**Date:** 2025-12-29

[📖 Read the Smart Daily Energy Manager README](./ai-built-agents/2025-12-29-smart-daily-energy-manager/README.md)

### Smart Exercise Companion

An adaptive agent that personalizes and optimizes exercise routines for everyday individuals to improve fitness and well-being.

**Category:** health

**Date:** 2025-12-28

[📖 Read the Smart Exercise Companion README](./ai-built-agents/2025-12-28-smart-exercise-companion/README.md)

### Smart Medication Manager

A smart assistant that ensures you never miss a dose and keeps track of medication schedules effortlessly.

**Category:** health

**Date:** 2025-12-26

[📖 Read the Smart Medication Manager README](./ai-built-agents/2025-12-26-smart-medication-manager/README.md)

### Smart Bill Tracker

Effortlessly manage and track all your bills to avoid late fees and stress.

**Category:** finance

**Date:** 2025-12-26

[📖 Read the Smart Bill Tracker README](./ai-built-agents/2025-12-26-smart-bill-tracker/README.md)

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

