from twilio.rest import Client
import os


class NotificationManager:
    def __init__(self):
        dotenv_path = "credentials.env"
        with open(dotenv_path, "r") as f:
            for line in f:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value

    def send_notification(self, price, city_name):
        account_sid = os.getenv("ACCOUNT_SID")
        auth_token = os.getenv("AUTH_TOKEN")
        self.client = Client(account_sid, auth_token)
        message = self.client.messages.create(
            body=f"Low price alert! \nOnly {price}€ to fly_from {city_name}",
            from_='+14237197546',
            to='+919409498914'
        )
        print(message.sid)
