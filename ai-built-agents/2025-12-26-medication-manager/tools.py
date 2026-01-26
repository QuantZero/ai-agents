from twilio.rest import Client
from schemas import ReminderOutput
import os

# Send SMS tool
def send_sms_reminder(reminder: ReminderOutput):
    client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
    message = client.messages.create(
        body=f"Reminder: It's time to take your medication {reminder.medication_name} at {reminder.time}.",
        from_=os.getenv('TWILIO_PHONE_NUMBER'),
        to=os.getenv('USER_PHONE_NUMBER')
    )
    print(f"Sent reminder: {message.sid}")
