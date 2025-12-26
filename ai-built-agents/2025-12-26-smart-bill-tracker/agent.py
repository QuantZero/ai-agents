# agent.py

import os
import datetime
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from schemas import Bill, UserSettings
from graph import BillStateMachine
from pydantic import ValidationError

load_dotenv()

class SmartBillTracker:
    def __init__(self, user_email: str, twilio_client):
        self.user_email = user_email
        self.twilio_client = twilio_client
        self.state_machine = BillStateMachine()

    def send_email_reminder(self, bill: Bill):
        try:
            msg = MIMEText(f"Reminder: Your bill for {bill.name} is due on {bill.due_date}.")
            msg['Subject'] = 'Bill Payment Reminder'
            msg['From'] = os.getenv('EMAIL_SENDER')
            msg['To'] = self.user_email

            with smtplib.SMTP(os.getenv('SMTP_SERVER'), os.getenv('SMTP_PORT')) as server:
                server.starttls()
                server.login(os.getenv('EMAIL_SENDER'), os.getenv('EMAIL_PASSWORD'))
                server.send_message(msg)

            print(f"Email reminder sent for {bill.name}.")
        except Exception as e:
            print(f"Failed to send email reminder: {e}")

    def send_sms_reminder(self, bill: Bill):
        try:
            message = self.twilio_client.messages.create(
                body=f"Reminder: Your bill for {bill.name} is due on {bill.due_date}.",
                from_=os.getenv('TWILIO_PHONE_NUMBER'),
                to=os.getenv('USER_PHONE_NUMBER')
            )
            print(f"SMS reminder sent for {bill.name}.")
        except Exception as e:
            print(f"Failed to send SMS reminder: {e}")

    def track_bills(self, user_settings: UserSettings):
        try:
            for bill in user_settings.bills:
                self.state_machine.process_bill(bill)
                if bill.due_date <= datetime.date.today() + datetime.timedelta(days=user_settings.reminder_days):
                    self.send_email_reminder(bill)
                    self.send_sms_reminder(bill)
        except ValidationError as e:
            print(f"Validation error: {e}")

if __name__ == "__main__":
    import argparse
    from twilio.rest import Client

    parser = argparse.ArgumentParser(description='Smart Bill Tracker')
    parser.add_argument('user_email', type=str, help='User email for sending reminders')
    args = parser.parse_args()

    twilio_client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
    tracker = SmartBillTracker(args.user_email, twilio_client)

    # Example user settings
    user_settings = UserSettings(
        user_email=args.user_email,
        bills=[
            Bill(name='Electricity', amount=100.0, due_date=datetime.date(2023, 11, 25)),
            Bill(name='Water', amount=30.0, due_date=datetime.date(2023, 11, 28))
        ],
        reminder_days=3
    )
    tracker.track_bills(user_settings)
