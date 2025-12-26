from langgraph import Graph, State
from prompts import system_prompt, user_prompt_template
from schemas import FocusInput, FocusOutput


class AnalyzeFocusState(State):
    def run(self, input_data: FocusInput) -> FocusOutput:
        # Simulate interaction with an LLM
        response = f"Based on your input: {input_data.user_input}, here are some tips to improve your focus..."
        return FocusOutput(focus_advice=response)


focus_graph = Graph()
focus_graph.add_state('analyze_focus', AnalyzeFocusState())
focus_graph.set_initial_state('analyze_focus')
