from langgraph import StateMachine
from prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE
from schemas import ParentingInput, ParentingOutput


class ParentingStateGraph(StateMachine):
    def __init__(self, openai_client):
        super().__init__()
        self.openai_client = openai_client

    def run(self, user_input: ParentingInput) -> ParentingOutput:
        prompt = USER_PROMPT_TEMPLATE.format(
            child_name=user_input.child_name,
            age=user_input.age,
            preferences=user_input.preferences,
            health_info=user_input.health_info
        )

        response = self.openai_client.generate(prompt=SYSTEM_PROMPT + "\n" + prompt)

        # Dummy parsing logic
        meal_plan = "Vegetarian lunch with vegetables and rice."
        activity_suggestion = "Outdoor play in the park."
        health_advice = "Avoid peanuts due to allergy."

        return ParentingOutput(
            meal_plan=meal_plan,
            activity_suggestion=activity_suggestion,
            health_advice=health_advice
        )
