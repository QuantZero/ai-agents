# Smart Digital Declutterer

## Summary
The Smart Digital Declutterer is an AI agent designed to help manage digital clutter by organizing files and emails efficiently.

## Problem It Solves
Many people struggle with overwhelming digital clutter from files and emails, leading to stress, wasted time, and decreased productivity. This agent addresses these issues by automating the organization process.

## How It Works
The agent provides tools to organize files into directories based on file types and to declutter email inboxes by categorizing emails. It uses a command-line interface where users can specify whether to organize files or emails.

## Example Use Case
A user can run the agent to clean up their desktop by organizing files into folders or sorting their email inbox into categories such as Work, Personal, and Spam.

## How to Run
1. Clone the repository.
2. Create a `.env` file with the necessary email credentials.
3. Run the agent using the command:
   - `python agent.py file <directory>` to organize files.
   - `python agent.py email` to organize emails.

## Tech Stack Used
- Python
- Pydantic for data validation
- LangGraph for state management
- OpenAI for potential future enhancements
- dotenv for managing environment variables
