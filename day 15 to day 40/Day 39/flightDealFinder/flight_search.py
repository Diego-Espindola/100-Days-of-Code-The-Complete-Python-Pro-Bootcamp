import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    token_url = 'https://test.api.amadeus.com/v1/security/oauth2/token'

    # Dados para obter o token
    data = {
        'grant_type': 'client_credentials',
        'client_id': 'ZR4TCJwaRgWAQrKcG4njpXCroQdRGkpr',  # Substitua pelo seu API Key
        'client_secret': 'O1r8dp8BArdNzWFT'  # Substitua pelo seu API Secret
    }

    # Enviando a solicitação POST para obter o token
    response = requests.post(token_url, data=data)

    # Verificando se a solicitação foi bem-sucedida
    if response.status_code == 200:
        token = response.json().get('access_token')
        print('Token de acesso obtido com sucesso!')
    else:
        print('Falha ao obter o token. Status code:', response.status_code)
        print('Detalhes:', response.text)

    # URL da API de busca de voos
    search_url = 'https://test.api.amadeus.com/v2/shopping/flight-offers'

    # Cabeçalhos com o token de acesso
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # Parâmetros para a busca de voos
    params = {
        'originLocationCode': 'BPS',  # Código IATA da cidade de origem
        'destinationLocationCode': 'FLN',  # Código IATA da cidade de destino
        'departureDate': '2025-03-01',  # Data de partida no formato YYYY-MM-DD
        'adults': 1
    }

    # Enviando a solicitação GET para buscar voos
    response = requests.get(search_url, headers=headers, params=params)

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
