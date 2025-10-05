import pandas as pd
import ollama
from datetime import datetime 


df = pd.read_csv("vancouver_weather.csv")
df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')

# Example: pick the 15:00 row
row = df[df['datetime'].dt.hour == 15].iloc[0]

#Prompt
prompt = f"""
Weather at {row['datetime']}:
Temperature: {row['temp_C']}°C
Condition: {row['condition']}
Humidity: {row['humidity']}%
Wind speed: {row['wind_speed_m_s']} m/s

Write a fun, friendly comment for the user based on the weather.
"""

response = ollama.chat(model="gemma:2b", messages=[{"role": "user", "content": prompt}])
print(response.message.content)
