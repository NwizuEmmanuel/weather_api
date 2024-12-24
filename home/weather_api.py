from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
api_key = os.getenv("API_KEY")
weather_location = "Lagos"
api_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{weather_location}?unitGroup=us&key={api_key}&contentType=json"
api_request = requests.get(api_url)

data = api_request.json()

def get_weather_api():
    units = {
        "windspeed": "km/h",
        "precip": "mm",
        "humidity": "%",
        "temp": "C"
    }
    api_data = {
        "resolvedAddress": data["resolvedAddress"],
        "timezone": data["timezone"],
        "description": data["description"],
        "days":[]
    }
    day_data = {
        "datetime": "",
        "temp": 0,
        "precip": 0,
        "humidity": 0,
        "windspeed": 0,
        "description": ""
    }

    for day in data["days"]:
        day_data["datetime"] = day["datetime"]
        day_data["temp"] = day["temp"]
        day_data["precip"] = day["precip"]
        day_data["humidity"] = day["humidity"]
        day_data["windspeed"] = day["windspeed"]
        day_data["description"] = day["description"]
        api_key["days"].append(day_data)

    return api_key, units
