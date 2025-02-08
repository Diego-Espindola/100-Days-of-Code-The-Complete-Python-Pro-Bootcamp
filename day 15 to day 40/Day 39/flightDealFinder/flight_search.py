import requests
import os
from dotenv import load_dotenv


load_dotenv()
CLIENT_SECRET = os.getenv('client_secret')
CLIENT_ID = os.getenv('client_id')
TOKEN_ENDPOINT = 'https://test.api.amadeus.com/v1/security/oauth2/token'
FLIGHT_ENDPOINT = 'https://test.api.amadeus.com/v2/shopping/flight-offers'

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        pass
    
    @staticmethod
    def get_flight_data(origin_location_code, destination_location_code, departure_date):    
        
        # Dados para obter o token
        data = {
            'grant_type': 'client_credentials',
            'client_id': CLIENT_ID,  # API Key
            'client_secret': CLIENT_SECRET  # API Secret
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


        # Cabeçalhos com o token de acesso
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

        # Parâmetros para a busca de voos
        params = {
            'originLocationCode': origin_location_code,  # Código IATA da cidade de origem
            'destinationLocationCode': destination_location_code,  # Código IATA da cidade de destino
            'departureDate': departure_date,  # Data de partida no formato YYYY-MM-DD
            'adults': 1,
            'nonStop':"true"
        }

        # Enviando a solicitação GET para buscar voos
        response = requests.get(FLIGHT_ENDPOINT, headers=headers, params=params)

        # Verificando se a solicitação foi bem-sucedida
        if response.status_code == 200:
            flight_data = response.json()
            print('Voos encontrados com sucesso!')

            # Iterando sobre as ofertas de voos e exibindo os preços
            for offer in flight_data.get('data', []):
                for itinerarie in offer["itineraries"]:
                    for segments in itinerarie["segments"]:
                        print(segments)

                # Acessando a estrutura de preços dentro das ofertas
                price = offer.get('price', {})
                total = price.get('total')
                currency = price.get('currency')

                # Exibindo informações de preços
                print(f"Preço: {total} {currency}")
        else:
            print('Falha ao buscar voos. Status code:', response.status_code)
            print('Detalhes:', response.text)


if(__name__ == '__main__'):
    FlightSearch.get_flight_data('FLN', 'BPS', '2025-06-02')