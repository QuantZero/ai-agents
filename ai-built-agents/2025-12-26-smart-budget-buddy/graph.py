from langgraph import Node, Graph
from prompts import RESPONSE_PROMPT

class BudgetAnalysisNode(Node):
    def process(self, data):
        # Here, integrate with OpenAI or any LLM for response generation
        # For demo purposes, we'll simulate a response
        income = data['income']
        expenses = sum(data['expenses'].values())
        savings = income - expenses

        if savings > 0:
            return {"recommendation": "You have a positive cash flow. Consider increasing your savings or investments."}
        else:
            return {"recommendation": "Your expenses exceed your income. Consider reducing discretionary spending."}

class BudgetGraph(Graph):
    def __init__(self):
        super().__init__()
        self.add_node("budget_analysis", BudgetAnalysisNode(), RESPONSE_PROMPT)
        self.set_start_node("budget_analysis")