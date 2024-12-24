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
print(f"Address: {data["resolvedAddress"]}; Timezone: {data["timezone"]}")
print(f"Description: {data["description"]}")

for day in data["days"]:
    print("==================")
    print("datetime:",day["datetime"])
    print(f"Temp: {day["temp"]}C")
    print(f"Precipitation: {day["precip"]}mm")
    print(f"Humidity: {day["humidity"]}%")
    print(f"Wind: {day["windspeed"]}km/h")
    print(f"Description: {day["description"]}")
