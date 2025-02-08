import requests
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN_ENDPOINT = 'https://test.api.amadeus.com/v1/security/oauth2/token'
FLIGHT_ENDPOINT = 'https://test.api.amadeus.com/v2/shopping/flight-offers'


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.client_secret = os.getenv('client_secret')
        self.client_id = os.getenv('client_id')
        self.token = self._get_new_token()
    

    def _get_new_token(self):
        # Dados para obter o token
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,  # API Key
            'client_secret': self.client_secret  # API Secret
        }

        # Enviando a solicitação POST para obter o token
        response = requests.post(TOKEN_ENDPOINT, data=data)
        # Verificando se a solicitação foi bem-sucedida
        if response.status_code == 200:
            token = response.json().get('access_token')
            print('Token de acesso obtido com sucesso!')
        else:
            print('Falha ao obter o token. Status code:', response.status_code)
            print('Detalhes:', response.text)
            token = ""

        return token


    def get_flight_data(self, origin_location_code, destination_location_code, departure_date):    
        
        # Cabeçalhos com o token de acesso
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

        # Parâmetros para a busca de voos
        params = {
            'originLocationCode': origin_location_code,  # Código IATA da cidade de origem
            'destinationLocationCode': destination_location_code,  # Código IATA da cidade de destino
            'departureDate': departure_date,  # Data de partida no formato YYYY-MM-DD
            'adults': 1,
            'nonStop':"false"
        }

        # Enviando a solicitação GET para buscar voos
        response = requests.get(FLIGHT_ENDPOINT, headers=headers, params=params)

        # Verificando se a solicitação foi bem-sucedida
        if response.status_code == 200:
            flight_data = response.json()
        else:
            print('Falha ao buscar voos. Status code:', response.status_code)
            print('Detalhes:', response.text)
            return None
        return flight_data


if(__name__ == '__main__'):
    FlightSearch.get_flight_data('FLN', 'BPS', '2025-03-01')
