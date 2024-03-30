from dotenv import load_dotenv
import requests
import os

load_dotenv()

GENDER = os.getenv('GENDER')
WEIGHT_KG = os.getenv('WEIGHT_KG')
HEIGHT_CM = os.getenv('HEIGHT_CM')
AGE = os.getenv('AGE')
APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
URL = os.getenv('NUTRITIONIX_URL')


class Nutritionix:

    def __init__(self):
        pass

    @staticmethod
    def request_exercise(query):

        request_headers = {
            "x-app-id": APP_ID,
            "x-app-key": API_KEY,
            "x-remote-user-id": "0"  # in development mode, set this to 0.
        }

        request_parameters = {
            "query": query,
            "gender": GENDER,
            "weight_kg": WEIGHT_KG,
            "height_cm": HEIGHT_CM,
            "age": AGE
        }

        response = requests.post(url=URL, headers=request_headers, json=request_parameters)
        response.raise_for_status()

        return response.json()
