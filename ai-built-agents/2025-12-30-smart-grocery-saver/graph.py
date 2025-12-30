# graph.py

from langgraph import LangGraph
from typing import Dict
from tools import optimize_shopping_list


def run_grocery_state_machine(input_data: Dict) -> Dict:
    # Initialize state machine
    graph = LangGraph()

    # Define state transitions
    graph.add_node("start", optimize_shopping_list)

    # Run the state machine from "start" node
    result = graph.run("start", input_data)
    return result
