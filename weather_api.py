from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_query = os.getenv("API_QUERY")
units = {
        "windspeed": "km/h",
        "precip": "mm",
        "humidity": "%",
        "temp": "C"
    }

def get_weather_api(location):
    api_request = None
    error = None
    try:
        api_request = requests.get(api_query)
    except Exception as e:
        error = e

    data = api_request.json()
    today_data = data["days"][0]
    api_data = {
        "resolvedAddress": data["resolvedAddress"],
        "timezone": data["timezone"],
        "description": data["description"],
        "datetime": today_data["datetime"],
        "temp": today_data["temp"],
        "precip": today_data["precip"],
        "humidity": today_data["humidity"],
        "windspeed": today_data["windspeed"],
        "description": today_data["description"]
    }

    return {"api_data": api_data, "error": error}
