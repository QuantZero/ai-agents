# Agent Builder 2.0

**Agent Builder 2.0** - An autonomous AI engineer that builds comprehensive, production-ready full-stack applications.

## Overview

Agent Builder 2.0 is a complete rewrite focused on building **comprehensive end-to-end full-stack solutions** rather than small utility scripts. Each build results in a complete, deployable application with frontend, backend, database, and deployment strategy.

This agent runs on a fixed daily schedule and automatically:
1. Generates a novel, comprehensive full-stack application idea
2. Designs proper architecture (frontend, backend, database, deployment)
3. Implements a complete, production-ready application
4. Creates comprehensive documentation
5. Updates the registry
6. Commits and pushes to GitHub
7. Sends a summary email

Each daily run results in a **complete, deployable full-stack application** that follows modern best practices and is ready for production use.

## What's New in 2.0

### 🎯 Focus on Comprehensive Solutions
- **Full-stack applications** with frontend, backend, and database
- **Production-ready architecture** with proper separation of concerns
- **Complete user workflows** from start to finish
- **Deployment-ready** with Docker and cloud configurations

### 🏷️ Professional Naming
- **No more "Smart" prefix** - uses descriptive, professional names
- Examples: "TaskFlow", "ExpenseTracker", "HealthMonitor"
- Names reflect the core value proposition

### 🏗️ Better Architecture
- Proper design patterns (MVC, service layers, repositories)
- RESTful API design or GraphQL
- Database schema design with migrations
- Authentication and authorization
- Error handling, logging, and monitoring
- Testing infrastructure

### 📦 Complete Tech Stacks
- Modern frontend frameworks (React, Vue, Next.js)
- Robust backend frameworks (FastAPI, Express, Django)
- Appropriate database choices (PostgreSQL, MongoDB)
- Proper authentication strategies
- Deployment configurations

## Features

- 🤖 **Autonomous Operation**: Runs daily at a scheduled time
- 🎯 **Comprehensive Solutions**: Builds complete full-stack applications
- 💎 **Production-Ready**: Implements proper architecture and best practices
- 🏗️ **Modern Tech Stacks**: Uses appropriate frameworks and tools
- 📚 **Auto-Documentation**: Creates comprehensive READMEs and updates registry
- 🔄 **Git Integration**: Automatically commits and pushes to GitHub
- 📧 **Email Reports**: Always sends reports (success or error) to developer

## Architecture

The agent uses LangGraph to orchestrate a multi-step workflow:

1. **Idea Generation**: Uses LLM to generate a comprehensive full-stack application idea
2. **Architecture Design**: Designs proper architecture with frontend, backend, database, and deployment
3. **Implementation**: Generates complete application code following best practices
4. **File Writing**: Creates application directory structure with all necessary files
5. **Registry Update**: Updates main README with new application entry
6. **Git Commit**: Commits and pushes changes
7. **Email Report**: Always sends a report (success or error) to configured recipient

**Focus Areas**: The agent prioritizes comprehensive solutions:
- Productivity & workflow management
- Data management & analytics
- Content creation & publishing
- E-commerce & marketplace
- Social & collaboration platforms
- Learning & education platforms
- Health & wellness tracking
- Finance & budgeting systems
- Project management & collaboration
- Communication & messaging platforms

## Requirements

- Python 3.12+
- `uv` package manager (recommended) or `pip`
- OpenAI API key
- Git repository initialized
- (Optional) Email configuration for summaries

## Quick Start

### Installation

From the `agent-builder` directory:

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the `agent-builder` directory:

```env
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional - Model selection
OPENAI_MODEL=gpt-4o

# Optional - Email configuration
EMAIL_RECIPIENT=your_email@example.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password

# Optional - Schedule time (HH:MM format)
DAILY_RUN_TIME=09:00

# Optional - GitHub repo URL for links in emails
GITHUB_REPO_URL=https://github.com/yourusername/yourrepo
```

### Running

**One-time execution:**
```bash
python main.py
```

**Scheduled daily execution:**
```bash
python main.py --schedule
```

This will run the agent at the time specified in `DAILY_RUN_TIME` (default: 09:00).

## Output Structure

Each application is created in `ai-built-agents/YYYY-MM-DD-application-slug/` with:

```
application-name/
├── frontend/          # Frontend application files
├── backend/           # Backend API files
├── database/          # Database schema and migrations
├── docs/              # Additional documentation
├── docker-compose.yml # Deployment configuration (if applicable)
├── README.md          # Comprehensive documentation
└── .env.example       # Environment variables template
```

## Naming Conventions

Agent Builder 2.0 uses professional, descriptive names:

✅ **Good Examples:**
- `TaskFlow` - Task management application
- `ExpenseTracker` - Expense tracking system
- `HealthMonitor` - Health tracking platform
- `LearningPath` - Educational platform
- `HomeHub` - Home management system

❌ **Avoid:**
- `SmartTaskManager` - Generic "Smart" prefix
- `AIBudgetApp` - Generic "AI" prefix
- `AutoHealthTracker` - Generic "Auto" prefix

## What Gets Built

Each application includes:

1. **Frontend**
   - Modern framework (React, Vue, Next.js, etc.)
   - Routing and navigation
   - State management
   - API integration
   - Error handling
   - Responsive design

2. **Backend**
   - RESTful or GraphQL API
   - Authentication and authorization
   - Data validation
   - Error handling
   - Logging
   - Database integration

3. **Database**
   - Proper schema design
   - Relationships
   - Indexes
   - Migrations (if applicable)

4. **Configuration**
   - Environment variables
   - Deployment settings
   - Docker configuration (if applicable)

5. **Documentation**
   - Comprehensive README
   - API documentation
   - Architecture overview
   - Deployment guide

## Workflow Details

### 1. Idea Generation
The agent generates a comprehensive application idea that:
- Solves a real, substantial problem
- Requires a full-stack solution
- Has clear user value
- Uses professional naming

### 2. Architecture Design
Designs proper architecture with:
- Frontend framework selection
- Backend framework selection
- Database choice
- Authentication strategy
- Deployment strategy

### 3. Implementation
Generates complete code with:
- All necessary files for frontend, backend, and database
- Proper structure and organization
- Best practices and patterns
- Error handling and validation
- Documentation

### 4. File Writing
Creates the complete directory structure with all files.

### 5. Registry Update
Updates both:
- `ai-built-agents/README.md`
- Main repository `README.md`

### 6. Git Commit
Commits and pushes changes with a descriptive message.

### 7. Email Report
Sends a comprehensive report (success or error) to the configured recipient.

## Scheduling

### Cron Job (Linux/Mac)

Add to your crontab:

```bash
0 9 * * * cd /path/to/agent-builder && /usr/bin/python3 main.py
```

### GitHub Actions

See `GITHUB_ACTIONS_SETUP.md` for detailed GitHub Actions setup instructions.

## Project Structure

```
agent-builder/
├── main.py              # Main entry point
├── graph.py             # LangGraph workflow definition
├── prompts.py           # LLM prompts for idea generation and implementation
├── schemas.py           # Pydantic schemas for state management
├── tools.py             # File operations, git, and email utilities
├── pyproject.toml       # Dependencies
├── README.md            # This file
└── .env                 # Configuration (gitignored)
```

## Error Handling

The agent includes comprehensive error handling:
- Errors are tracked throughout the workflow
- Partial completions are handled gracefully
- Error reports are sent via email
- All errors are logged for debugging

## Contributing

Agent Builder 2.0 is designed to be autonomous, but improvements are welcome:
- Better prompt engineering
- Additional tech stack support
- Enhanced error handling
- Documentation improvements

## License

See the main repository license.

## Changelog

### 2.0.0
- Complete rewrite focusing on full-stack applications
- Professional naming conventions (no "Smart" prefix)
- Comprehensive architecture design
- Production-ready code generation
- Better error handling and reporting

### 1.0.0
- Initial release
- Daily agent generation
- Basic functionality
