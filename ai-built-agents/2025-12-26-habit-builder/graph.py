# graph.py

from langgraph import State, Transition, Graph
from schemas import HabitState

class HabitBuilderGraph(Graph):
    def __init__(self):
        states = [
            State(name='start', on_enter=self.start_habit),
            State(name='track_progress', on_enter=self.track_progress),
            State(name='complete', on_enter=self.complete_habit),
        ]
        transitions = [
            Transition(source='start', destination='track_progress'),
            Transition(source='track_progress', destination='complete', condition=self.is_habit_complete)
        ]
        super().__init__(states=states, transitions=transitions)

    def start_habit(self, state: HabitState):
        print(f"Starting habit: {state.habit_name}")

    def track_progress(self, state: HabitState):
        state.current_step += 1
        print(f"Day {state.current_step}/{state.total_days}: Keep it up!")

    def complete_habit(self, state: HabitState):
        print(f"Congratulations! You've completed the habit: {state.habit_name}")

    def is_habit_complete(self, state: HabitState):
        return state.current_step >= state.total_days
