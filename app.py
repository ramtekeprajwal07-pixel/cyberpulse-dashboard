from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Weather API endpoint (Free Open-Meteo API)
@app.route('/api/weather/<city>')
def get_weather(city):
    cities = {
        "nagpur": {"lat": 21.1458, "lon": 79.0882},
        "mumbai": {"lat": 19.0760, "lon": 72.8777},
        "delhi": {"lat": 28.6139, "lon": 77.2090},
        "london": {"lat": 51.5074, "lon": -0.1278},
        "tokyo": {"lat": 35.6762, "lon": 139.6503}
    }
    
    city_lower = city.lower()
    coords = cities.get(city_lower, cities["nagpur"])
        
    url = f"https://api.open-meteo.com/v1/forecast?latitude={coords['lat']}&longitude={coords['lon']}&current_weather=true&hourly=temperature_2m"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return jsonify(response.json())
        return jsonify({"error": "Failed to fetch data"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)