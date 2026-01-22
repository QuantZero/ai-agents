from langgraph import StateMachine, State
from schemas import HydrationInput, HydrationOutput
from prompts import SYSTEM_PROMPT, USER_PROMPT

class HydrationStateMachine(StateMachine):
    def __init__(self, llm):
        self.llm = llm
        super().__init__(initial_state=self.initial_state)

    def initial_state(self, input_data: HydrationInput) -> State:
        prompt = USER_PROMPT.format(weight_kg=input_data.weight_kg, activity_level=input_data.activity_level)
        response = self.llm.complete(prompt=SYSTEM_PROMPT + "\n" + prompt)
        recommended_water_intake_liters = self.parse_response(response)
        return State(output=HydrationOutput(recommended_water_intake_liters=recommended_water_intake_liters))

    def parse_response(self, response: str) -> float:
        # Example parsing logic, assuming the response contains only the number
        try:
            return float(response.strip())
        except ValueError:
            raise ValueError("Invalid response format from LLM")