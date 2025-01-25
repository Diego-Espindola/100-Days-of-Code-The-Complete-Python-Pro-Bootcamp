import requests
from info import sheety_id

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        url_get: str = f"https://api.sheety.co/${sheety_id}/flightDealsProject/prices"

    def get_data_sheet(self):
        pass
