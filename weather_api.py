from dotenv import load_dotenv
import os
import redis.client
import requests
import redis
import json

redis_hostname = os.getenv("HOSTNAME")
redis_port = os.getenv("PORT")
redis_db = os.getenv("DB")

r = redis.Redis(
    host=redis_hostname,
    port=redis_port,
    db=redis_db
)

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

def get_weather_api(location):
    api_query = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=us&key={api_key}&contentType=json"
    api_request = requests.get(api_query)
    
    if api_request.status_code != 200:
        return {
            "api_data": None,
            "error": f"API request failed with status {api_request.status_code}: {api_request.text}"
        }
    
    try:
        data = api_request.json()
    except ValueError:
        return {
            "api_data": None,
            "error": "Failed to decode JSON from response."
        }
    today_data = data.get("days", [{}])[0]
    api_data = {
        "resolvedAddress": data["resolvedAddress"],
        "timezone": data["timezone"],
        "description": data["description"],
        "temp": today_data["temp"],
        "precip": today_data["precip"],
        "humidity": today_data["humidity"],
        "windspeed": today_data["windspeed"],
    }
    json_string = json.dumps(api_data)
    r.sadd("weather_api", json_string)
    cache_data = r.smembers("weather_api")
    
    json_data_from_cache = json.loads(cache_data)
    return {"api_data": json_data_from_cache, "error": None}

def save_to_cache():
    r.sadd("weather_api", get_weather_api())