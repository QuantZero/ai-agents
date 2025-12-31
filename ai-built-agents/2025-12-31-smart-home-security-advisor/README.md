# Smart Home Security Advisor

## Summary
The Smart Home Security Advisor is an AI agent that evaluates the security of your home based on crime data specific to your location, providing tailored security advice.

## Problem It Solves
Millions of homeowners face the threat of burglary and intrusion. Many are unaware of vulnerabilities in their security setup or how to effectively address them. This agent provides insights into the safety of their neighborhood and suggests security measures accordingly.

## How It Works
1. User inputs their address.
2. The agent fetches crime data for the address.
3. It evaluates the crime data and generates security advice.
4. The advice is presented to the user, helping them make informed decisions about their home security.

## Example Use Case
A homeowner enters their address into the system. The agent evaluates the local crime data and suggests that the homeowner should install additional lighting and surveillance based on a high crime score.

## How to Run It
1. Install dependencies using Poetry: `poetry install`
2. Create a `.env` file using the `.env.example` template and add your OpenAI API key.
3. Run the agent: `python agent.py <address>`

## Tech Stack
- **Python**: Main programming language
- **Pydantic**: For data validation
- **LangChain OpenAI**: For AI capabilities
- **Requests**: To fetch crime data from APIs
- **dotenv**: To manage environment variables
