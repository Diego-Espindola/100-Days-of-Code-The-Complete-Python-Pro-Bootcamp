import requests
import os
from dotenv import load_dotenv

load_dotenv()
SHEETY_ID = os.getenv('sheety_id')

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url_get: str = f"https://api.sheety.co/{SHEETY_ID}/flightDealsProject/prices"
        self.destination_data = {}

    def get_destination_data(self):
        try:
            response = requests.get(self.url_get)
            data = response.json()
            self.destination_data = data['prices']
        except Exception as e:
            print('Erro ao buscar dados na planilha ', e)
            return self.destination_data
