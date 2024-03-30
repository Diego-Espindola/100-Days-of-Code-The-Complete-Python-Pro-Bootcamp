from datetime import datetime
from dotenv import load_dotenv
import requests
import os

current_date = datetime.today()
DAY = current_date.strftime("%d/%m/%Y")
HOUR = current_date.strftime("%H:%M:%S")

load_dotenv()
AUTHORIZATION = os.getenv('AUTHORIZATION')
URL = os.getenv('SHEETY_URL')


class Sheety:

    def __init__(self):
        pass

    @staticmethod
    def add_new_row(exercise, duration, calories, date=DAY, time=HOUR):

        request_headers = {
            "Content-Type": "application/json",
            "Authorization": AUTHORIZATION
        }
        body = {
            "page": {
                "date": date,
                "time": time,
                "exercise": exercise,
                "duration": duration,
                "calories": calories
            }
        }

        response = requests.post(url=URL, headers=request_headers, json=body)
        response.raise_for_status()
