from langgraph import State, Transition, StateMachine
from schemas import ScheduleInput, Task

class OptimizeScheduleState(State):
    def execute(self, data: ScheduleInput):
        # Sort tasks by importance and fit them into available time
        sorted_tasks = sorted(data.tasks, key=lambda x: x.importance, reverse=True)
        total_time = 0
        optimized_schedule = []
        for task in sorted_tasks:
            if total_time + task.duration <= data.available_time:
                optimized_schedule.append({"task": task.name, "start_time": total_time})
                total_time += task.duration
        return optimized_schedule

optimize_schedule = StateMachine(
    initial_state=OptimizeScheduleState(),
    transitions=[Transition(from_state=OptimizeScheduleState, to_state=None)]  # End after optimization
)
