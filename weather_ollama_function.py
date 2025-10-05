import pandas as pd
from datetime import datetime
import subprocess

def generate_weather_comment(city_csv):
    df = pd.read_csv(city_csv)
    df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')

    row = df[df['datetime'].dt.hour == 15].iloc[0]

    prompt = f"""
    Weather at {row['datetime']}:
    Temperature: {row['temp_C']}°C
    Condition: {row['condition']}
    Humidity: {row['humidity']}%
    Wind speed: {row['wind_speed_m_s']} m/s

    Write a fun, friendly comment for the user based on the weather.
    """

    # Call Ollama from subprocess instead of import
    result = subprocess.run(
        ["ollama", "run", "gemma:2b", "--prompt", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()
