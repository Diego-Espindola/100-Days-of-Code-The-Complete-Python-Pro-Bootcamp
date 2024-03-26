import requests
import json
from info import token, USERNAME
from datetime import date
# Site to see the pixe.la
# https://pixe.la/v1/users/diegoesp/graphs/graph1.html


pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = 'graph1'
request_header = {
    "X-USER-TOKEN": token
}


def create_user():
    user_params = {
        "token": token,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)


def create_graph():

    request_body = {
        "id": GRAPH_ID,
        "name": "Lecture Graph",
        "unit": "Pages",
        "type": "int",
        "color": "kuro",
        "timezone": "Brazil/West"
    }

    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

    response = requests.post(url=graph_endpoint, headers=request_header, json=request_body)
    print(response.text)


def add_info(quantity, graph_id=GRAPH_ID):
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
    current_date = date.today().strftime("%Y%m%d")
    request_body = {
        "date": current_date,
        "quantity": f"{quantity}"
    }
    response = requests.post(url=graph_endpoint, headers=request_header, json=request_body)
    response_json = json.loads(response.text)
    if response_json["message"] == "This date pixel already exist.":
        update_value(quantity)
    else:
        print(response.text)


def delete_graph(graph_id=GRAPH_ID):
    url = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
    response = requests.delete(url=url, headers=request_header)
    print(response.text)


def update_value(quantity, graph_id=GRAPH_ID):
    url = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
    response = requests.delete(url=url, headers=request_header)
    print(response.text)


pages = input("How many pages did you read today?")
add_info(quantity=pages)
