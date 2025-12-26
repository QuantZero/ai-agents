from langgraph import StateMachine, State

class StressManagementFlow(StateMachine):
    def __init__(self):
        super().__init__()
        self.initial_state = State(name="initial")
        self.advice_state = State(name="advice")
        self.final_state = State(name="final")

        self.add_transition(self.initial_state, self.advice_state, self.collect_stress_data)
        self.add_transition(self.advice_state, self.final_state, self.provide_advice)

    def collect_stress_data(self, input_data):
        # Logic to collect stress data from the user
        return "Data collected"

    def provide_advice(self, input_data):
        # Logic to provide advice
        return "Advice given"