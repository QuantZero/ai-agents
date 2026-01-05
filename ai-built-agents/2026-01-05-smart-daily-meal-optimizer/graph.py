from langgraph import Graph, State
from prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

class MealOptimizerGraph(Graph):
    def __init__(self, api_key: str):
        self.api_key = api_key
        super().__init__(initial_state=self.start_state())

    def start_state(self) -> State:
        return State(name="start", on_enter=self.generate_meal_plan)

    def generate_meal_plan(self, input_data):
        # This is where the OpenAI API interaction would occur
        user_prompt = USER_PROMPT_TEMPLATE.format(
            preferences=input_data.dietary_preferences,
            budget=input_data.budget
        )
        # Mock response for demonstration
        response = {"meals": ["Grilled tofu salad", "Vegetarian chili", "Quinoa and black bean stir-fry"]}
        return response