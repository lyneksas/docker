from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

# === API informacija ===
WEATHER_API_KEY = "d3a9fdc03f9388fdfbf283425a58ec42"  # OpenWeather API raktas
CURRENCY_API_KEY = "3e0181179f99b54475201bd1"  # ExchangeRate API raktas
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

# === Kešai ===
weather_cache = {}
exchange_cache = {}
CACHE_EXPIRY = 600  # 10 minučių

# === Šalis -> valiuta ===
country_currency_map = {
    "US": "USD", "LT": "EUR", "GB": "GBP", "PL": "PLN", "DE": "EUR", "FR": "EUR",
    "SE": "SEK", "NO": "NOK", "JP": "JPY", "CN": "CNY", "IN": "INR", "UA": "UAH",
    "LV": "EUR", "EE": "EUR", "RU": "RUB"
}

# === Orų gavimo funkcija ===
def get_weather(city):
    current_time = time.time()
    if city in weather_cache:
        data, timestamp = weather_cache[city]
        if current_time - timestamp < CACHE_EXPIRY:
            return data

    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric",
        "lang": "lt"
    }

    try:
        response = requests.get(WEATHER_API_URL, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()
            weather_cache[city] = (data, current_time)
            return data
        else:
            return None
    except:
        return None

# === Valiutos gavimo funkcija ===
def get_exchange_rate(currency_code):
    current_time = time.time()
    if currency_code in exchange_cache:
        rate, timestamp = exchange_cache[currency_code]
        if current_time - timestamp < CACHE_EXPIRY:
            return rate

    url = f"https://v6.exchangerate-api.com/v6/{CURRENCY_API_KEY}/latest/{currency_code}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        rate = data.get("conversion_rates", {}).get("EUR")
        if rate:
            exchange_cache[currency_code] = (rate, current_time)
            return rate
        return None
    except:
        return None

# === Flask maršrutas ===
@app.route("/api/info")
def api_info():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Miesto parametras privalomas"}), 400

    weather = get_weather(city)
    if not weather:
        return jsonify({"error": "Nepavyko gauti orų duomenų"}), 404

    country_code = weather["sys"].get("country")
    currency_code = country_currency_map.get(country_code)
    rate = get_exchange_rate(currency_code) if currency_code else None

    return jsonify({
        "city": weather["name"],
        "country": country_code,
        "temperature": weather["main"]["temp"],
        "weather": weather["weather"][0]["description"],
        "wind": weather["wind"]["speed"],
        "currency": currency_code,
        "eur_rate": rate
    })

# === Paleidimas ===
if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5000, debug=True)
    
