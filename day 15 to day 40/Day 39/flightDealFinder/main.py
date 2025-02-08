#This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from datetime import datetime, timedelta
from data_manager import DataManager as SheetyApiDataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager


ORIGIN_CITY_IATA = "FLN"


def main():
    sheety_api_data_manager = SheetyApiDataManager()
    sheety_api_data_manager.get_destination_data()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()
    print("Sheet data",sheety_api_data_manager.destination_data)

    tomorrow = datetime.now() + timedelta(days=1)
    for destination in sheety_api_data_manager.destination_data:
        print(f"Getting flights for {destination}")
        flights = flight_search.get_flight_data(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            tomorrow.strftime("%Y-%m-%d")
        )
        cheapest_flight = find_cheapest_flight(flights)
        if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
            print(f"Lower price flight found to {destination['city']}!")
            notification_manager.send_sms(
                message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                            f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                            f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
            )
            # Trying whatsapp instead.
            #notification_manager.send_whatsapp(
            #    message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
            #                f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
            #                f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
            #)


if __name__ == "__main__":
    main()
