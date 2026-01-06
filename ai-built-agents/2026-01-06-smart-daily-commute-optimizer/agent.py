# agent.py

import os
import sys
import requests
from dotenv import load_dotenv
from schemas import CommuteRequest, CommuteResponse
from graph import CommuteFlow

load_dotenv()

API_KEY = os.getenv('TRAFFIC_API_KEY')

class SmartDailyCommuteOptimizer:
    def __init__(self):
        self.flow = CommuteFlow()

    def run(self, start_location: str, end_location: str):
        try:
            commute_request = CommuteRequest(start_location=start_location, end_location=end_location)
            response = self.flow.execute(commute_request)
            print(response)
        except Exception as e:
            print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python agent.py <start_location> <end_location>")
        sys.exit(1)
    start_location, end_location = sys.argv[1], sys.argv[2]
    optimizer = SmartDailyCommuteOptimizer()
    optimizer.run(start_location, end_location)
