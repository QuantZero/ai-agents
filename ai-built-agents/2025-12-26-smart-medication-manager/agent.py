import os
import sys
from dotenv import load_dotenv
from typing import List
from langgraph import LangGraph
from schemas import MedicationInput, ReminderOutput
from tools import send_sms_reminder

# Load environment variables
load_dotenv()

# Error handling
try:
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
    USER_PHONE_NUMBER = os.getenv('USER_PHONE_NUMBER')
    if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, USER_PHONE_NUMBER]):
        raise EnvironmentError("One or more environment variables are not set.")
except EnvironmentError as e:
    sys.exit(f"Environment Error: {e}")

# Main execution logic
def main(medications: List[MedicationInput]):
    graph = LangGraph()
    # Define the states and transitions
    graph.add_state('start', on_enter=check_medications)
    graph.add_state('send_reminder', on_enter=send_reminders)
    graph.add_state('complete')

    graph.add_transition('start', 'send_reminder', condition=has_medications_due)
    graph.add_transition('send_reminder', 'complete')

    # Start the state machine
    graph.run('start', medications=medications)

def check_medications(context):
    # Logic to check for due medications
    context['due_medications'] = [med for med in context['medications'] if med.is_due()]


def has_medications_due(context):
    return len(context['due_medications']) > 0

def send_reminders(context):
    for med in context['due_medications']:
        reminder = ReminderOutput(medication_name=med.name, time=med.time)
        send_sms_reminder(reminder)

if __name__ == "__main__":
    # Example medications list
    medications = [MedicationInput(name="Aspirin", time="08:00", phone_number=USER_PHONE_NUMBER),
                   MedicationInput(name="Insulin", time="20:00", phone_number=USER_PHONE_NUMBER)]
    main(medications)
