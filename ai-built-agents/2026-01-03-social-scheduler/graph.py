from langgraph import StateMachine, State
from schemas import ScheduleRequest, EventSuggestion, SchedulerState
from tools import CalendarAPI, CommunicationAPI

class SocialSchedulerGraph(StateMachine):
    def __init__(self, calendar_api: CalendarAPI, communication_api: CommunicationAPI):
        self.calendar_api = calendar_api
        self.communication_api = communication_api
        initial_state = SchedulerState(current_step="start")
        super().__init__(initial_state)

    def run(self, schedule_request: ScheduleRequest):
        self.state.current_step = "fetch_availabilities"
        availabilities = self.calendar_api.get_availabilities(schedule_request)

        self.state.current_step = "suggest_events"
        self.state.suggestions = self.suggest_events(availabilities)

        self.state.current_step = "notify_users"
        self.communication_api.notify_users(schedule_request.user_email, self.state.suggestions)

        return self.state.suggestions

    def suggest_events(self, availabilities):
        suggestions = []
        for day, time_slots in availabilities.items():
            for time_slot in time_slots:
                suggestions.append(EventSuggestion(day=day, time_slot=time_slot, participants=[]))  # Add logic to match participants
        return suggestions
