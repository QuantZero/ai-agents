# graph.py

from langgraph import State, StateMachine
from schemas import Bill

class BillStateMachine(StateMachine):
    def __init__(self):
        super().__init__(initial_state='new')

    def process_bill(self, bill: Bill):
        # Define simple state transitions for a bill
        self.add_transition('new', 'pending', self.is_pending(bill))
        self.add_transition('pending', 'due', self.is_due(bill))
        self.run()  # Run the state machine

    def is_pending(self, bill: Bill):
        return lambda: bill.due_date > datetime.date.today()

    def is_due(self, bill: Bill):
        return lambda: bill.due_date <= datetime.date.today()
