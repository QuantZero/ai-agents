from langgraph import StateMachine, State
from prompts import SYSTEM_PROMPT, USER_PROMPT
from tools import get_energy_optimization_recommendations

class EnergyOptimizationGraph(StateMachine):
    def __init__(self):
        super().__init__()
        self.add_state(State("start", self.collect_data))
        self.add_state(State("optimize", self.optimize_energy_usage), end_state=True)
        self.set_start("start")

    def collect_data(self, input_data):
        return "optimize", input_data

    def optimize_energy_usage(self, input_data):
        recommendations = get_energy_optimization_recommendations(
            SYSTEM_PROMPT,
            USER_PROMPT.format(
                current_temperature=input_data.current_temperature,
                energy_prices=input_data.energy_prices
            )
        )
        return recommendations
