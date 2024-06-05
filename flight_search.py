import os
import requests

class FlightSearch:
    def __init__(self):
        dotenv_path = "credentials.env"
        with open(dotenv_path, "r") as f:
            for line in f:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value  # set the environment variable of a key to value.

    def get_iata_code(self, city_name):
        tequila_endpoint = "https://api.tequila.kiwi.com/locations/query"
        parameters = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "airport",
            "active_only": "True",
        }
        headers = {"apikey": os.getenv("TAQUILA_API_KEY")}

        response = requests.get(tequila_endpoint, params=parameters, headers=headers)
        data = response.json()["locations"]
        if data:
            return data[0]["city"]["code"]
        return None
