from flask import Flask, render_template, request
from weather_ollama import generate_weather_comment

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        city = request.form.get("city")
        hour = request.form.get("hour")
        try:
            # hour = int(hour)
            hour = int(request.form.get("hour"))
            summary = generate_weather_comment("weather.csv", hour)
        except (TypeError, ValueError):
            hour = 15  # default fallback
        
        csv_path = "weather.csv"  # later you can map city → CSV
        result = generate_weather_comment(csv_path, hour=hour)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)

