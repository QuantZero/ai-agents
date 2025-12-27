# Smart Medication Manager

## Summary
The Smart Medication Manager is an AI agent that helps individuals manage their medication schedules by sending timely SMS reminders.

## Problem It Solves
For millions of people managing multiple medications, remembering to take each dose on time can be challenging. Missing doses can lead to serious health issues and non-compliance adversely affects health outcomes.

## How It Works
The agent uses a state machine to track medication schedules and send reminders via SMS when doses are due. Users input their medication schedule, and the agent checks the current time against these schedules to send reminders using Twilio's SMS service.

## Example Use Case
A user inputs their daily medications such as Aspirin at 08:00 and Insulin at 20:00. At these respective times, the user receives an SMS reminder to take their medication.

## How to Run It
1. Clone the repository.
2. Install dependencies with `poetry install`.
3. Configure the `.env` file with your Twilio credentials and phone numbers.
4. Run the agent using `python agent.py`.

## Tech Stack Used
- Python
- Pydantic
- LangGraph
- Twilio API
- Python-dotenv
