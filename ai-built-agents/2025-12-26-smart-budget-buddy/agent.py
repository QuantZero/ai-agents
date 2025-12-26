import os
import sys
from dotenv import load_dotenv
from langgraph import Graph
from schemas import BudgetInput, BudgetOutput
from prompts import BUDGET_PROMPT, RESPONSE_PROMPT

load_dotenv()

class SmartBudgetBuddy:
    def __init__(self):
        self.graph = Graph()

    def run(self, income: float, expenses: dict):
        try:
            input_data = BudgetInput(income=income, expenses=expenses)
            # Process through graph
            result = self.graph.process(input_data.dict(), BUDGET_PROMPT)
            output_data = BudgetOutput.parse_obj(result)
            return output_data
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python agent.py <income> <expenses>")
        sys.exit(1)

    income = float(sys.argv[1])
    expenses = {k: float(v) for k, v in (arg.split('=') for arg in sys.argv[2:])}
    agent = SmartBudgetBuddy()
    result = agent.run(income, expenses)
    print("Budget Recommendation:", result.recommendation)