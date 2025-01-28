#This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager as SheetyApiDataManager


def main():
    sheety_api_data_manager = SheetyApiDataManager()
    sheet_data = sheety_api_data_manager.get_destination_data()
    print(sheet_data)


if __name__ == "__main__":
    main()