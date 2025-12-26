# Dependency Conflict Resolver

## Summary
The Dependency Conflict Resolver is an AI agent designed to identify and resolve dependency conflicts in software projects, helping developers and DevOps engineers streamline their build processes and avoid deployment delays.

## Problem it Solves
Dependency conflicts are a common issue in software development, often leading to build failures and delaying deployments. This agent automates the detection and resolution of such conflicts, allowing developers to focus on feature development rather than troubleshooting dependency issues.

## How it Works
The agent takes a requirements file as input, identifies any version conflicts using a dependency checker library, and resolves these conflicts using a state machine defined with LangGraph. The current resolution strategy is to select the latest version of conflicting dependencies.

## Example Use Case
A developer working on a Python project runs into build failures due to conflicting dependency versions specified in the `requirements.txt` file. By running this agent, the developer can automatically detect and resolve these conflicts, ensuring a smooth build process.

## How to Run It
1. Ensure you have Python 3.8+ and Poetry installed.
2. Clone this repository.
3. Install dependencies using `poetry install`.
4. Run the agent: `python agent.py path/to/requirements.txt`

## Tech Stack Used
- Python
- Pydantic for data validation
- LangGraph for state machine management
- OpenAI for potential NLP tasks (future enhancement)
- Python-dotenv for environment variable management
