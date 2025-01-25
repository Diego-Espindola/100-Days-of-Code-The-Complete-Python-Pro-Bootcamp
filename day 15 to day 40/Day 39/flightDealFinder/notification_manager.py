from twilio.rest import Client
from info import phone_number, account_sid, auth_token, from_number


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
