# WeatherWise ☀️

WeatherWise is a friendly, interactive web app that provides hourly and daily weather summaries for your city. It also gives outfit suggestions and eco-friendly tips. The app dynamically updates its background based on the current weather and time of day, delivering fun and engaging messages with emojis.

---

## Features

- Hourly and daily weather summaries tailored to your city
- Friendly advice on what to wear based on temperature
- Sustainability tips like walking, biking, or reducing artificial lighting
- Dynamic backgrounds for sunny, cloudy, rainy, snowy, and night conditions
- Fun, engaging messages with emojis

---

## Installation

1. **Clone the repository:**

```bash
git clone <your-repo-url>
cd weatherwise
```
You should have files app.py, weather_extract.py, weather_ollama.py, index.html (the html file is in the templates folder).

2. **Create virtual environment:**
```bash
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```
3. **Install required Python libraries:**
- Install the Python libraries used in the app:

```bash
pip install pandas flask requests
```

4. **Install and set up Ollama**:
Download and install Ollama from https://ollama.com/download.
Make sure the Ollama CLI is accessible in your terminal.
Pull the LLM model in your terminal used in this app:
```bash
ollama pull gemma:2b
```

5 **Run the flask app in your terminal:**.
```bash
python app.py
```
Open your browser and go to http://127.0.0.1:5000/. Enter your city and the hour for the forecast. Receive a customized message with a weather summary and advice!
