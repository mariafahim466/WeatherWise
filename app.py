from flask import Flask, render_template
import requests

app = Flask(__name__)
API_KEY = "d6f4e57cb210cbd8edfd287897dfe058"

@app.route("/")
def home():
    # Example location
    lat = 49.25
    lon = -123.1

    # Fetch weather forecast
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    data = requests.get(url).json()

    # Take first forecast for simplicity
    forecast = data['list'][0]
    weather = {
        "time": forecast['dt_txt'],
        "temp": forecast['main']['temp'],
        "condition": forecast['weather'][0]['description']
    }

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
