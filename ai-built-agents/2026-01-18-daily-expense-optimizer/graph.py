from langgraph import Graph, Node
from tools import calculate_total_expenses, generate_advice

def define_graph() -> Graph:
    graph = Graph()
    
    # Define nodes
    input_node = Node(name="Input")
    total_expense_node = Node(name="Calculate Total Expenses", handler=calculate_total_expenses)
    advice_node = Node(name="Generate Advice", handler=generate_advice)
    output_node = Node(name="Output")

    # Connect nodes
    graph.connect(input_node, total_expense_node)
    graph.connect(total_expense_node, advice_node)
    graph.connect(advice_node, output_node)

    return graph
