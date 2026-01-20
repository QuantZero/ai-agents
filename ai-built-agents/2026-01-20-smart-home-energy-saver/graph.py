from langgraph import StateMachine
from prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

class EnergySaverFlow(StateMachine):
    def __init__(self, openai_client):
        super().__init__()
        self.openai_client = openai_client

    def run(self, input_data):
        # Generate user prompt
        user_prompt = USER_PROMPT_TEMPLATE.format(
            area_size=input_data.area_size,
            num_occupants=input_data.num_occupants,
            energy_rate=input_data.energy_rate
        )

        # Get response from OpenAI
        response = self.openai_client.complete(prompt=SYSTEM_PROMPT + user_prompt)

        # Return the suggestions
        return response.choices[0].text.strip()