# graph.py

from langgraph import StateMachine, State
from openai import OpenAI
from prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

class SleepOptimizerGraph(StateMachine):
    def __init__(self, input_data):
        self.input_data = input_data
        self.states = [
            State(name="start", on_enter=self.start_state),
            State(name="analyze_input", on_enter=self.analyze_input_state),
            State(name="provide_recommendations", on_enter=self.provide_recommendations_state, final=True)
        ]
        super().__init__(self.states, initial_state="start")

    def start_state(self):
        # Move to the next state
        self.transition_to("analyze_input")

    def analyze_input_state(self):
        # Perform analysis (placeholder for actual logic)
        self.transition_to("provide_recommendations")

    def provide_recommendations_state(self):
        # Generate recommendations using OpenAI
        user_prompt = USER_PROMPT_TEMPLATE.format(
            sleep_duration=self.input_data.sleep_duration,
            sleep_quality=self.input_data.sleep_quality,
            stress_level=self.input_data.stress_level,
            caffeine_intake=self.input_data.caffeine_intake,
            exercise_frequency=self.input_data.exercise_frequency
        )

        response = OpenAI.complete(prompt=SYSTEM_PROMPT + user_prompt)
        return {"recommendations": response}
