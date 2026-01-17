# graph.py

from langgraph import Graph, Node, Edge
from tools import AIResponseTool


def build_graph() -> Graph:
    # Define the nodes
    start_node = Node(name="Start", tool=AIResponseTool())
    end_node = Node(name="End")

    # Define the edges
    edge = Edge(source=start_node, target=end_node, condition=lambda x: True)

    # Create the graph
    graph = Graph(nodes=[start_node, end_node], edges=[edge])
    return graph
