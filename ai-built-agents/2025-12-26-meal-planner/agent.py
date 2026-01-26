# agent.py

import os
import sys
import logging
from dotenv import load_dotenv
from pydantic import ValidationError
from langgraph import Graph
from schemas import MealPlanInput
from graph import meal_planner_graph

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    # CLI Interface
    if len(sys.argv) < 2:
        logger.error("Usage: python agent.py <input_json>")
        sys.exit(1)
    
    input_data = sys.argv[1]
    
    try:
        # Validate input data
        meal_plan_input = MealPlanInput.parse_raw(input_data)
    except ValidationError as e:
        logger.error(f"Input validation error: {e}")
        sys.exit(1)
    
    # Execute the meal planner graph
    try:
        graph = Graph(meal_planner_graph)
        result = graph.run(meal_plan_input.dict())
        
        # Output the result
        logger.info("Meal Plan:")
        logger.info(result)
    except Exception as e:
        logger.error(f"Error executing meal planner: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()