import requests
import pandas as pd

# ----- SETTINGS -----
API_KEY = "3adaf830179ed47d5597c340dc46ee25"
CITY = "Coquitlam"

# ----- GET CURRENT WEATHER -----
current_url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(current_url)
current_data = response.json()

# Check for errors
if response.status_code != 200:
    print("Error fetching current weather:", current_data)
    exit()  # stop script

# Organize current weather
current_weather = {
    "datetime": [pd.Timestamp.now()],
    "type": ["current"],
    "temp_C": [current_data['main']['temp']],
    "condition": [current_data['weather'][0]['description']],
    "humidity": [current_data['main']['humidity']],
    "wind_speed_m_s": [current_data['wind']['speed']]
}

df_current = pd.DataFrame(current_weather)

# ----- GET 3-HOUR FORECAST -----
forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"
forecast_response = requests.get(forecast_url)
forecast_data = forecast_response.json()

if forecast_response.status_code != 200:
    print("Error fetching forecast:", forecast_data)
    exit()

forecast_list = []
for item in forecast_data['list']:
    forecast_list.append({
        "datetime": item['dt_txt'],
        "type": "forecast",
        "temp_C": item['main']['temp'],
        "condition": item['weather'][0]['description'],
        "humidity": item['main']['humidity'],
        "wind_speed_m_s": item['wind']['speed']
    })

df_forecast = pd.DataFrame(forecast_list)

# ----- COMBINE AND SAVE TO CSV -----
df = pd.concat([df_current, df_forecast], ignore_index=True)
df.to_csv("vancouver_weather.csv", index=False)

#print("CSV file 'vancouver_weather.csv' created successfully!")
