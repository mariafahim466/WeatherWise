from flask import Flask, render_template, request
from weather_ollama import generate_weather_comment

app = Flask(__name__)

IMG_MAP = {
    "sunny":  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8zdOXp7yfKWVv82Gjdxb_aIEkG6xbMy-5vw&s",
    "rainy":  "https://centralca.cdn-anvilcms.net/media/images/2019/01/02/images/Rainy_Weather_pix.max-1200x675.jpg",
    "snowy":  "https://images.unsplash.com/photo-1642209405880-e0acc64fe81f?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8c25vdyUyMGZhbGxpbmd8ZW58MHx8MHx8fDA%3D",
    "cloudy": "https://images.unsplash.com/photo-1501630834273-4b5604d2ee31",
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    city = None
    img_url = None

    if request.method == "POST":
        city = request.form.get("city")
        hour = request.form.get("hour")
        weather_type = request.form.get("weather_type")

        try:
            hour = int(hour)
        except (TypeError, ValueError):
            hour = 15

        csv_path = "weather.csv"
        result = generate_weather_comment(csv_path, hour=hour)
        img_url = IMG_MAP.get(weather_type, IMG_MAP["sunny"])

    return render_template("index.html", result=result, city=city, img_url=img_url)


if __name__ == "__main__":
    app.run(debug=True)
