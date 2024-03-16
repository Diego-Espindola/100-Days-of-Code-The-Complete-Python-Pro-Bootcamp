from twilio.rest import Client
from info import auth_token, account_sid, phone_number


def send_sms(body, to=phone_number):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
      from_="+17814233150",
      body=body,
      to=to
    )

    print(message.sid)
