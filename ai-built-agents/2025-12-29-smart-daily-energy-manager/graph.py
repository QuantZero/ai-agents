from langgraph import Graph, Node
from prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE
from langchain_openai import OpenAI

class EnergyFlow:
    def __init__(self):
        self.api = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.graph = Graph()
        self.setup_graph()

    def setup_graph(self):
        start_node = Node(name="start", action=self.analyze_energy)
        end_node = Node(name="end", action=self.generate_recommendations)

        self.graph.add_node(start_node)
        self.graph.add_node(end_node)
        self.graph.add_edge(start_node, end_node)

    def analyze_energy(self, user_data: dict) -> dict:
        # Analyze user data to understand energy patterns
        return {"analysis": "energy pattern analysis"}

    def generate_recommendations(self, analysis: dict) -> dict:
        # Generate recommendations based on analysis
        user_prompt = USER_PROMPT_TEMPLATE.format(user_data=analysis)
        response = self.api.generate(user_prompt, system=SYSTEM_PROMPT)
        return response

    def run(self, user_data: dict) -> dict:
        return self.graph.run(start_node_name="start", input_data=user_data)
