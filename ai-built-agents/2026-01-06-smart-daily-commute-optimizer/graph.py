# graph.py

from langgraph import StateMachine, Transition, State
from schemas import CommuteRequest, CommuteResponse
from tools import fetch_traffic_data, calculate_optimal_route

class CommuteFlow(StateMachine):
    def __init__(self):
        super().__init__(initial_state='start')
        
        self.states = {
            'start': State(on_enter=self.get_traffic_data, on_exit=None),
            'calculate_route': State(on_enter=self.get_optimal_route, on_exit=None),
            'end': State(on_enter=None, on_exit=None)
        }

        self.transitions = [
            Transition(source='start', target='calculate_route', condition=self.has_traffic_data),
            Transition(source='calculate_route', target='end', condition=self.has_optimal_route)
        ]

    def get_traffic_data(self, request: CommuteRequest):
        traffic_data = fetch_traffic_data(request.start_location, request.end_location)
        self.context['traffic_data'] = traffic_data
        self.transition('calculate_route')

    def get_optimal_route(self, request: CommuteRequest):
        optimal_route = calculate_optimal_route(request.start_location, request.end_location, self.context['traffic_data'])
        self.context['optimal_route'] = optimal_route
        self.transition('end')

    def has_traffic_data(self):
        return 'traffic_data' in self.context

    def has_optimal_route(self):
        return 'optimal_route' in self.context

    def execute(self, request: CommuteRequest) -> CommuteResponse:
        self.context = {}
        self.transition('start')
        return CommuteResponse(
            estimated_time=self.context['optimal_route']['estimated_time'],
            optimal_route=self.context['optimal_route']['route_description'],
            traffic_conditions=self.context['traffic_data']['conditions']
        )
