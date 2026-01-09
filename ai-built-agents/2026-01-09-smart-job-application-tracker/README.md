# Smart Job Application Tracker

## Summary
The Smart Job Application Tracker is an AI-driven agent designed to help job seekers efficiently track and manage their job applications. It prevents missed opportunities by organizing application details, deadlines, and follow-ups.

## Problem it Solves
Job seekers often apply to multiple positions simultaneously, making it challenging to keep track of each application's status and deadlines. This can lead to missed opportunities or increased stress. The Smart Job Application Tracker provides a structured way to manage these applications, ensuring users do not overlook important follow-ups or deadlines.

## How it Works
The agent uses a state machine to process and update the status of job applications. Users provide a JSON file containing application details, and the agent organizes and tracks the status, updating it as necessary. The agent provides an overview of application statuses, indicating where follow-up actions are needed.

## Example Use Case
A job seeker applies to 10 different companies. They use the Smart Job Application Tracker to input their applications. The agent processes this data, updates statuses, and advises on follow-ups, helping the user manage their job search efficiently.

## How to Run It
1. Install dependencies using `poetry install`.
2. Prepare a JSON file with job application data.
3. Run the agent: `python agent.py <path_to_job_applications.json>`.

## Tech Stack Used
- **Python**: Core programming language
- **Pydantic**: Used for data validation and management
- **LangGraph**: Utilized for the state machine that processes job applications
- **Langchain-OpenAI**: Optional integration for advanced processing (not used in this basic implementation)
- **Python-dotenv**: For managing environment variables
