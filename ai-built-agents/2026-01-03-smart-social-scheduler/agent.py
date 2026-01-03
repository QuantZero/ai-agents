import os
import sys
import logging
from dotenv import load_dotenv
from schemas import ScheduleRequest, EventSuggestion
from graph import SocialSchedulerGraph
from tools import CalendarAPI, CommunicationAPI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Main entry point for the Smart Social Scheduler
def main(input_json):
    try:
        # Parse input
        schedule_request = ScheduleRequest.parse_raw(input_json)
        
        # Initialize tools
        calendar_api = CalendarAPI()
        communication_api = CommunicationAPI()
        
        # Initialize state machine
        scheduler_graph = SocialSchedulerGraph(calendar_api, communication_api)
        
        # Execute scheduling logic
        suggestions = scheduler_graph.run(schedule_request)
        
        # Return suggestions
        return [suggestion.dict() for suggestion in suggestions]
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python agent.py '<input_json>'")
        sys.exit(1)
    input_json = sys.argv[1]
    output = main(input_json)
    print(output)
