import os
import sys
import openai
from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError
from langgraph import Graph
from schemas import ExpenseInput, ExpenseOutput
from graph import define_graph

# Load environment variables
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

class SmartDailyExpenseOptimizer:
    def __init__(self):
        self.graph = define_graph()

    def process_expense(self, expense_input: ExpenseInput) -> ExpenseOutput:
        try:
            # Validate input
            input_data = ExpenseInput(**expense_input)
            # Process through graph
            output_data = self.graph.run(input_data.dict())
            return ExpenseOutput(**output_data)
        except ValidationError as e:
            print("Input validation error:", e)
            sys.exit(1)
        except Exception as e:
            print("An error occurred:", e)
            sys.exit(1)

    def run(self):
        # Example CLI input
        expense_input = {
            "income": 3000,
            "fixed_expenses": {
                "rent": 1000,
                "utilities": 200
            },
            "variable_expenses": {
                "groceries": 300,
                "entertainment": 150
            },
            "savings_goal": 500
        }

        # Process the expense
        output = self.process_expense(expense_input)
        print("Optimized Expense Output:", output.json(indent=2))


if __name__ == "__main__":
    optimizer = SmartDailyExpenseOptimizer()
    optimizer.run()
