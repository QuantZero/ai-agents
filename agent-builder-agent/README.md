# Agent Builder Agent

**Agent Foundry** - An autonomous AI engineer that designs, builds, documents, and ships one new AI agent every day.

## Overview

This agent runs on a fixed daily schedule and automatically:
1. Generates a novel, practical AI agent use case
2. Implements it as a production-ready Python agent
3. Creates proper documentation
4. Updates the registry
5. Commits and pushes to GitHub
6. Sends a summary email

Each daily run results in a complete, working agent that follows modern best practices and is ready for use.

## Features

- 🤖 **Autonomous Operation**: Runs daily at a scheduled time
- 🎯 **High-Value Ideas**: Generates agents that solve critical problems for large audiences
- 💎 **Elegant Solutions**: Focuses on everyday problems that improve living standards
- 🏗️ **Production-Ready**: Implements agents with proper structure, typing, and documentation
- 📚 **Auto-Documentation**: Creates comprehensive READMEs and updates registry
- 🔄 **Git Integration**: Automatically commits and pushes to GitHub
- 📧 **Email Reports**: Always sends reports (success or error) to developer

## Architecture

The agent uses LangGraph to orchestrate a multi-step workflow:

1. **Idea Generation**: Uses LLM to generate a novel, high-value agent idea for large audiences
2. **Implementation**: Generates complete agent code following standards
3. **File Writing**: Creates agent directory structure and files
4. **Registry Update**: Updates main README with new agent entry
5. **Git Commit**: Commits and pushes changes
6. **Email Report**: Always sends a report (success or error) to configured recipient

**Focus Areas**: The agent prioritizes problems affecting millions of people:
- Health & wellness, Personal finance, Education & learning
- Productivity & time management, Communication & relationships
- Safety & security, Home & lifestyle, Career development
- Mental health & well-being, Accessibility & inclusion

## Requirements

- Python 3.12+
- `uv` package manager (recommended) or `pip`
- OpenAI API key
- Git repository initialized
- (Optional) Email configuration for summaries

## Installation

From the `agent-builder-agent` directory:

```bash
uv sync
```

Or with `pip`:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the `agent-builder-agent` directory:

```env
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Email Configuration (Required for email sending)
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_gmail_app_password
EMAIL_RECIPIENT=your_email@gmail.com  # Where to send reports

# Optional
OPENAI_MODEL=gpt-4o  # Default: gpt-4o
DAILY_RUN_TIME=09:00  # Default: 09:00 (24-hour format)
GITHUB_REPO_URL=https://github.com/user/repo  # For email links
SMTP_SERVER=smtp.gmail.com  # Default: smtp.gmail.com
SMTP_PORT=587  # Default: 587
```

**Note**: All email reports are sent to the address configured in `EMAIL_RECIPIENT`. This includes:
- Success reports (what was created, why, and how)
- Error reports (what failed, why, and how to fix)

**Gmail Setup**: To send emails via Gmail, you need to:
1. Enable 2-factor authentication on your Google account
2. Generate an App Password: https://myaccount.google.com/apppasswords
3. Use the app password (not your regular password) as `SMTP_PASSWORD`
4. Set `EMAIL_RECIPIENT` to the address where you want to receive reports

## Usage

### One-Time Execution

Run the agent builder once:

```bash
python main.py
```

### Scheduled Daily Execution

Run the agent builder on a daily schedule:

```bash
python main.py --schedule
```

This will:
- Run immediately if past the scheduled time
- Then run daily at the time specified in `DAILY_RUN_TIME` (default: 09:00)

To stop the scheduled execution, press `Ctrl+C`.

### Using System Scheduler (Recommended)

For production use, it's recommended to use your system's scheduler:

**macOS (launchd):**
```bash
# Create a plist file for launchd
# Run daily at 9:00 AM
```

**Linux (cron):**
```bash
# Add to crontab (crontab -e)
0 9 * * * cd /path/to/agent-builder-agent && /usr/bin/python3 main.py
```

## Agent Structure

Each generated agent follows this structure:

```
ai-projects/
  ai-built-agents/
    README.md                    # Registry of all built agents
    YYYY-MM-DD-agent-name/
      README.md                  # Comprehensive documentation
      agent.py                   # Main entry point
      schemas.py                 # Pydantic models (if needed)
      prompts.py                 # Prompts (if needed)
      graph.py                   # LangGraph workflow (if needed)
      tools.py                   # Tools (if needed)
      pyproject.toml             # Dependencies
      .env.example               # Environment variables template (if needed)
  agent-builder-agent/
    ├── main.py
    └── ...
```

## Generated Agent Standards

All generated agents follow these standards:

- **Language**: Python only
- **Stack**: pydantic, langgraph, modern LLM clients
- **Architecture**: Clear separation of concerns
- **Code Quality**: Type hints, docstrings, error handling
- **Configuration**: Environment variables, no hardcoded secrets
- **Documentation**: Comprehensive READMEs

## Registry

The main `README.md` acts as a public registry. Each day, a new entry is added with:
- Date
- Agent name
- Description
- Category
- Link to agent folder

Entries are never overwritten and maintained chronologically.

## Workflow Details

### Idea Generation

The agent generates ideas that:
- Solve distinct problems (no duplicates)
- Are implementable in a focused scope
- Are realistic for real-world usage
- Clearly justify why an agent is needed

### Implementation

Generated agents include:
- Clean file structure
- Proper error handling
- Type hints throughout
- Environment variable configuration
- Comprehensive documentation

### Git Integration

The agent:
- Adds all new files
- Creates a descriptive commit message
- Pushes to the remote repository
- Handles errors gracefully

## Error Handling & Reporting

The agent tracks errors at each step and always sends an email report:
- **Success Reports**: Sent when agent is successfully built, including:
  - What was created (agent description and functionality)
  - Why it exists (problem solved and value for large audiences)
  - How it works (architecture and implementation approach)
- **Error Reports**: Sent when any step fails, including:
  - What happened (summary of the run and failure point)
  - Why it failed (detailed error explanation)
  - How to fix it (suggested solutions)

All reports are sent to the address configured in `EMAIL_RECIPIENT` environment variable. The workflow always completes the email step, even if earlier steps failed.

## Example Output

```
============================================================
Agent Foundry - Daily Build
Date: 2024-01-15 09:00:00
============================================================

Found 4 existing agents
Starting workflow...

============================================================
Workflow Summary
============================================================
Idea Generated: True
Implementation Created: True
Files Written: True
Registry Updated: True
Git Committed: True
Email Sent: True

Agent Built: Code Review Agent
Location: /path/to/ai-built-agents/2024-01-15-code-review-agent

============================================================

✅ Daily agent build completed successfully!
```

## Troubleshooting

### OpenAI API Key Not Found

Ensure `OPENAI_API_KEY` is set in your `.env` file or environment.

### Git Operations Fail

- Ensure the repository is initialized (`git init`)
- Ensure you have a remote configured (`git remote add origin ...`)
- Check that you have push permissions

### Email Not Sending

Email sending requires SMTP configuration:
1. Set `SMTP_USER` to your Gmail address
2. Set `SMTP_PASSWORD` to a Gmail app password (not your regular password)
3. Generate app password at: https://myaccount.google.com/apppasswords

If SMTP is not configured, the email content will be printed to the console instead.

### Agent Generation Fails

Check the error messages in the workflow summary. Common issues:
- Invalid JSON in LLM response (should be rare with GPT-4o)
- File permission errors
- Disk space issues

## Development

To modify the agent builder:

- **Prompts**: Edit `prompts.py`
- **Workflow**: Edit `graph.py`
- **Tools**: Edit `tools.py`
- **Schemas**: Edit `schemas.py`

## Tech Stack

- **pydantic**: Data validation and schemas
- **langgraph**: Workflow orchestration
- **langchain-openai**: LLM integration
- **python-dotenv**: Environment variable management
- **schedule**: Daily scheduling (optional)

## License

See repository license.

## Notes

- The agent builder itself is a meta-agent that builds other agents
- Each generated agent is independent and self-contained
- The registry README is automatically maintained
- All agents follow consistent patterns and standards

