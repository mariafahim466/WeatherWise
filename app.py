from flask import Flask, render_template, request
from weather_ollama import generate_weather_comment

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    city = None
    if request.method == "POST":
        city = request.form.get("city")  # capture user input
        hour = request.form.get("hour")
        try:
            hour = int(hour)
        except (TypeError, ValueError):
            hour = 15
        
        csv_path = "weather.csv"
        result = generate_weather_comment(csv_path, hour=hour)
    
    # Pass the city variable to the template
    return render_template("index.html", result=result, city=city)

if __name__ == "__main__":
    app.run(debug=True)
