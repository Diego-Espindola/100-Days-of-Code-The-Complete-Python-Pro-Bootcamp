import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from info import subject, sender, email, password
import pandas as pd
import datetime as dt
import random as r


def send_email(body, receiver):

    # Create message
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject

    # Attach body to message
    message.attach(MIMEText(body, "plain"))

    # Connects
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Login, send email an quit
    server.login(email, password)
    server.sendmail(sender, receiver, message.as_string())
    server.quit()

    print("Email sent successfully!")


today = dt.datetime.now()
df = pd.read_csv('birthdays.csv')
today_birth = df[(df['month'] == today.month) & (df['day'] == today.day)]

if not today_birth.empty:
    letters = ['/letter_1.txt', '/letter_2.txt', '/letter_3.txt']
    for idx, person in today_birth.iterrows():
        _name = person['name']
        _email = person['email']
        random_letter = f"./letter_templates{r.choice(letters)}"
        with open(random_letter) as file:
            letter_content = file.read()
        letter_content = letter_content.replace('[NAME]', _name)
        send_email(letter_content, _email)
