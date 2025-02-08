from twilio.rest import Client
import os
from dotenv import load_dotenv


load_dotenv()
phone_number = os.getenv('phone_number')
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
from_number = os.getenv('from_number')


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    @staticmethod
    def send_sms(body, to=phone_number):
        client = Client(account_sid, auth_token)

        try:
            client.messages.create(
                from_=from_number,
                body=body,
                to=to
            )
            print("Message sent successfully!")
        except Exception as e:
            print(f"Error sending SMS: {e}")
