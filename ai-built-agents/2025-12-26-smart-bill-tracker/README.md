# Smart Bill Tracker

## Summary
Smart Bill Tracker is an AI-powered agent that helps users manage their monthly bills by sending timely reminders via email and SMS. It ensures that users never miss a payment, reducing financial stress and avoiding penalties.

## Problem It Solves
Many individuals struggle with tracking multiple monthly bills, leading to late payments and financial penalties. Smart Bill Tracker organizes bill information and sends reminders before due dates to prevent these issues.

## How It Works
Users provide their bill details and contact information. The agent processes this information and sets up reminders based on user preferences. It sends notifications via email and SMS before the bill's due date.

## Example Use Case
A user inputs their electricity and water bills into the system with due dates and an email address. Smart Bill Tracker sends a reminder three days before the due date, ensuring the user has enough time to make payments.

## How to Run It
1. Clone the repository.
2. Set up environment variables as per `.env.example`.
3. Install dependencies with `poetry install`.
4. Run the agent with `python agent.py <your-email@example.com>`.

## Tech Stack Used
- Python
- Pydantic for data modeling and validation
- LangGraph for state management
- OpenAI API (via Langchain-OpenAI) for potential future enhancements
- Twilio API for SMS notifications
- SMTP for email notifications
