import pandas as pd
import ollama
from datetime import datetime

import pandas as pd
import ollama
from datetime import datetime

def generate_weather_comment(csv_path, hour=15):
    df = pd.read_csv(csv_path)
    df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')

    # Pick row for the given hour
    df['hour'] = df['datetime'].dt.hour
    closest_idx = (df['hour'] - hour).abs().idxmin()
    row = df.loc[closest_idx]

    # row = matching_rows.iloc[0]

    # Build the prompt
    prompt = f"""
    Weather at {row['datetime']}:
    Temperature: {row['temp_C']}°C
    Condition: {row['condition']}
    Humidity: {row['humidity']}%
    Wind speed: {row['wind_speed_m_s']} m/s
    """

    if 'sunrise_local' in df.columns and not pd.isna(row.get('sunrise_local')):
        prompt += f"Sunrise: {row['sunrise_local']}\n"
    if 'sunset_local' in df.columns and not pd.isna(row.get('sunset_local')):
        prompt += f"Sunset: {row['sunset_local']}\n"
    if 'hours_of_sunlight' in df.columns and not pd.isna(row.get('hours_of_sunlight')):
        prompt += f"Hours of Sunlight: {round(row['hours_of_sunlight'], 2)}\n"

    prompt += "\nWrite a fun, friendly comment for the user based on the weather.\n"

    # Call Ollama
    response = ollama.chat(model="gemma:2b", messages=[{"role": "user", "content": prompt}])
    comment = response.message.content

    # Debug check
    print(f"✅ Weather for {row['datetime']} | Temp: {row['temp_C']}°C | Condition: {row['condition']}")
    print(f"🤖 LLM says: {comment}")

    # Return structured data
    return {
        "datetime": row['datetime'],
        "temp": row['temp_C'],
        "condition": row['condition'],
        "humidity": row['humidity'],
        "wind_speed": row['wind_speed_m_s'],
        "comment": comment
    }
