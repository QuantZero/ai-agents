# agent.py

import os
import sys
import logging
from dotenv import load_dotenv
from langgraph import Graph, Node
from geopy.geocoders import Nominatim
from schemas import DisasterPreparednessInput, DisasterPreparednessOutput
from prompts import SYSTEM_PROMPT, USER_PROMPT
from tools import get_disaster_guide

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

class SmartDisasterPreparednessPlanner:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="disaster_preparedness")
        self.graph = self._build_graph()

    def _build_graph(self) -> Graph:
        graph = Graph()
        # Define graph nodes and transitions using langgraph
        start_node = Node("start", self._get_location_info)
        guide_node = Node("get_guide", self._get_disaster_guide)
        graph.add_edge(start_node, guide_node)
        return graph

    def _get_location_info(self, input_data: DisasterPreparednessInput) -> DisasterPreparednessInput:
        location = self.geolocator.geocode(input_data.address)
        if location:
            input_data.latitude = location.latitude
            input_data.longitude = location.longitude
        return input_data

    def _get_disaster_guide(self, input_data: DisasterPreparednessInput) -> DisasterPreparednessOutput:
        guide = get_disaster_guide(input_data.latitude, input_data.longitude)
        return DisasterPreparednessOutput(guide=guide)

    def run(self, address: str):
        input_data = DisasterPreparednessInput(address=address)
        output_data = self.graph.run(input_data)
        print("Preparedness Guide:", output_data.guide)


def main():
    if len(sys.argv) < 2:
        print("Usage: python agent.py <address>")
        sys.exit(1)

    address = sys.argv[1]

    try:
        planner = SmartDisasterPreparednessPlanner()
        planner.run(address)
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()