import os
import sys
import logging
from dotenv import load_dotenv
from schemas import JobApplication
from graph import JobTrackerGraph

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Main execution logic
def main(file_path: str):
    # Load job applications
    try:
        applications = JobApplication.load_from_file(file_path)
        logger.info(f"Loaded {len(applications)} job applications.")
    except Exception as e:
        logger.error(f"Failed to load job applications: {str(e)}")
        sys.exit(1)

    # Initialize the job tracker agent
    tracker_agent = JobTrackerGraph()
    result = tracker_agent.run(applications)

    # Output results
    logger.info("Job Application Tracking Results:")
    for app in result:
        logger.info(f"Application to {app.company_name} - Status: {app.status}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python agent.py <path_to_job_applications.json>")
        sys.exit(1)
    file_path = sys.argv[1]
    main(file_path)
