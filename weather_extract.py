import requests
import pandas as pd
from datetime import datetime, timedelta, timezone

# ----- SETTINGS -----
API_KEY = "d2d03096e391a7efc9987f42e8bd7831"
CITY = "Tokyo"  # later set this to dynamic city variable

# ----- GET CURRENT WEATHER -----
current_url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(current_url)
current_data = response.json()

# Check current weather response
# HTTP status code 200 means the request was successful
if response.status_code != 200:
    print("Error fetching current weather:", current_data)
    exit()  # stop script

# Extract timezone offset in seconds
tz_offset = current_data['timezone']

# Convert sunrise/sunset to city local time using timezone-aware datetime
sunrise_local = datetime.fromtimestamp(current_data['sys']['sunrise'], tz=timezone.utc) + timedelta(seconds=tz_offset)
sunset_local = datetime.fromtimestamp(current_data['sys']['sunset'], tz=timezone.utc) + timedelta(seconds=tz_offset)

# Calculate hours of sunlight
hours_of_sunlight = (sunset_local - sunrise_local).total_seconds() / 3600

# Organize current weather + sunlight info
current_weather = {
    "datetime": [datetime.now(timezone.utc) + timedelta(seconds=tz_offset)],  # current local time
    "type": ["current"],
    "temp_C": [current_data['main']['temp']],
    "condition": [current_data['weather'][0]['description']],
    "humidity": [current_data['main']['humidity']],
    "wind_speed_m_s": [current_data['wind']['speed']],
    "sunrise_local": [sunrise_local],
    "sunset_local": [sunset_local],
    "hours_of_sunlight": [hours_of_sunlight]
}

df_current = pd.DataFrame(current_weather)

# ----- GET 3-HOUR FORECAST -----
forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"
forecast_response = requests.get(forecast_url)
forecast_data = forecast_response.json()

# Check forecast response
# HTTP status code 200 means the request was successful
if forecast_response.status_code != 200:
    print("Error fetching forecast:", forecast_data)
    exit()

forecast_list = []
for item in forecast_data['list']:
    forecast_list.append({
        "datetime": datetime.strptime(item['dt_txt'], "%Y-%m-%d %H:%M:%S") + timedelta(seconds=tz_offset),  # convert to city local time
        "type": "forecast",
        "temp_C": item['main']['temp'],
        "condition": item['weather'][0]['description'],
        "humidity": item['main']['humidity'],
        "wind_speed_m_s": item['wind']['speed']
    })

df_forecast = pd.DataFrame(forecast_list)

# ----- COMBINE AND SAVE TO CSV -----
df = pd.concat([df_current, df_forecast], ignore_index=True)
df.to_csv("weather.csv", index=False)

print(f"CSV file 'weather.csv' created successfully!")

