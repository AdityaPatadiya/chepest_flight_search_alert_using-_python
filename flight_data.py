import os
import requests
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


class FlightData:
    def __init__(self):
        self.lowestprice = []
        self.datamanager = DataManager()
        self.flightsearch = FlightSearch()
        self.notificationmanager = NotificationManager()
        dotenv_path = "credentials.env"
        with open(dotenv_path, "r") as f:
            for line in f:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value  # set the environment variable of key to value.

    def get_flight_price(self):
        data = self.datamanager.get_data()

        for item in data:
            city = item["city"]
            code = self.flightsearch.get_iata_code(city)
            tequila_endpoint = "https://api.tequila.kiwi.com/v2/search"
            parameters = {
                "fly_from": code,
                "fly_to": "RAJ",
                "date_from": "17/06/2024",
                "date_to": "19/06/2024",
                "curr": "INR",
            }
            headers = {"apikey": os.getenv("TAQUILA_API_KEY")}

            response = requests.get(tequila_endpoint, params=parameters, headers=headers)
            pprint(response.json())
            price = response.json()["data"][0]["price"]
            print(price, city)
            # if price < item["lowestPrice"]:
            #     self.notificationmanager.send_notification(price, city)


FlightData().get_flight_price()
