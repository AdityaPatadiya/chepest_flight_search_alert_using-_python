import os
import requests
from flight_search import FlightSearch
from pprint import pprint


class DataManager:
    def __init__(self):
        self.data = []
        self.flight_search = FlightSearch()
        dotenv_path = "credentials.env"
        with open(dotenv_path, "r") as f:
            for line in f:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value

    def get_data(self):
        sheet_endpoint = "https://api.sheety.co/9d7b4a6b4f40269f127c50fc53de5e80/capstoneProject/prices"
        response = requests.get(sheet_endpoint, auth=(os.getenv("USERNAME"), os.getenv("PASSWORD")))
        self.data = response.json()["prices"]  # all the data
        return self.data

    def update_iata_codes(self):
        self.get_data()
        for item in self.data:
            city_name = item["city"]
            iata_code = self.flight_search.get_iata_code(city_name)
            self.update_sheet_iata_code(item["id"], iata_code)

    def update_sheet_iata_code(self, object_id, iata_code):
        sheet_endpoint = f"https://api.sheety.co/9d7b4a6b4f40269f127c50fc53de5e80/capstoneProject/prices/{object_id}"
        sheet_inputs = {"prices": {"iataCode": iata_code}}
        response = requests.put(sheet_endpoint, json=sheet_inputs, auth=(os.getenv("USERNAME"), os.getenv("PASSWORD")))
        print(response.text)  # Print response to see if the update was successful
