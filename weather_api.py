from dotenv import load_dotenv
import os
import requests
import caching

load_dotenv() # load environment variables
api_key = os.getenv("API_KEY") # get api key


if not api_key:
    raise ValueError("API KEY is not set. Check your .env file.")

units = {
        "windspeed": "km/h",
        "precip": "inch",
        "humidity": "%",
        "temp": "F"
    }
error_message  = None

def get_weather_api(location):
    api_query = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=us&key={api_key}&contentType=json"
    api_request = requests.get(api_query)
    
    if api_request.status_code != 200:
        error_message = f"API request failed with status {api_request.status_code}: {api_request.text}"
        return False

    try:
        data = api_request.json()
    except ValueError:
        error_message = "Failed to decode JSON from response."
        return False

    today_data = data.get("days", [{}])[0]
    api_data = {
        "resolvedAddress": data["resolvedAddress"],
        "description": data["description"],
        "temp": today_data["temp"],
        "precip": today_data["precip"],
        "humidity": today_data["humidity"],
        "windspeed": today_data["windspeed"],
    }
    caching.cache_to_redis(api_data)
    return True
