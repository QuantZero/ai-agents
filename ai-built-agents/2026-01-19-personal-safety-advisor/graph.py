from langgraph import StateMachine, State, Transition


class SafetyAdvisorStateMachine(StateMachine):
    def __init__(self):
        self.initial_state = State(name="Awaiting Location Input")
        self.safety_advice_state = State(name="Providing Safety Advice")

        self.transitions = [
            Transition(
                trigger="location_received",
                source=self.initial_state,
                target=self.safety_advice_state
            )
        ]
        super().__init__(initial_state=self.initial_state, states=[self.initial_state, self.safety_advice_state])