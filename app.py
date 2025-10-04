from flask import Flask, render_template, request

app = Flask(__name__)

# Replace this with your teammates' CSV + LLM code
def generate_weather_summary(city):
    # Example placeholder logic
    return f"WeatherBuddy says: It looks sunny in {city} today! 🌞"

@app.route("/", methods=["GET"])
def home():
    city = request.args.get("city")
    summary = None
    if city:
        summary = generate_weather_summary(city)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
