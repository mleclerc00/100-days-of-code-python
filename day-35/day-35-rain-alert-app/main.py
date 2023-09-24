import os

import requests
from twilio.rest import Client

# https://www.twilio.com/docs/libraries/python
# auth_sid, auth_token, twilio_phone_number, and my_phone_number are environment variables
auth_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
twilio_phone_number = os.environ["TWILIO_PHONE_NUMBER"]
my_phone_number = os.environ["MY_PHONE_NUMBER"]

# tomorrow.io API docs: https://docs.tomorrow.io/reference/data-layers-overview
weather_api_endpoint = "https://api.tomorrow.io/v4/weather/forecast"

# params for the weather API
weather_params = {
    "location": os.environ["CITY"],
    "apikey": os.environ["API_KEY"],
}

# make the request to the weather API
response = requests.get(weather_api_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# get forecast for the next 12 hours
weather_data = weather_data["timelines"]["hourly"][:12]

# get the weather code for each hour
weather_codes = [hour["values"]["weatherCode"] for hour in weather_data]

# weather codes: https://docs.tomorrow.io/reference/data-layers-overview#weather-codes
# if any of the weather codes are 4000 or above, send a text
if any(code >= 4000 for code in weather_codes):
    # create a Twilio client
    client = Client(auth_sid, auth_token)
    # create a message
    message = client.messages.create(
        body="It's going to rain, remember to bring an umbrella! ☔️",
        from_=twilio_phone_number,
        to=my_phone_number,
    )
    print(message.status)
