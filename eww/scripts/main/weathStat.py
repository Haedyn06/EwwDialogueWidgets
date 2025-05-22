import requests
import datetime
import pytz
import requests_cache

# === CONFIG ===
API_KEY = "2875b641a67343638cf232032252205"  # Your WeatherAPI key
LOCATION = "Calgary"
TIMEZONE = "America/Edmonton"
URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={LOCATION}&aqi=no"

# === CACHE SETUP (optional, expires after 60s) ===
requests_cache.install_cache('weather_cache', expire_after=60)

# === CHECK DAY OR NIGHT ===
def isDay():
    now = datetime.datetime.now(pytz.timezone(TIMEZONE))
    return 6 <= now.hour < 18

# === ICON MAPPING ===
def getWeather(condition, daytime):
    condition = condition.lower()
    if "clear" in condition or "sunny" in condition:
        return "☀︎" if daytime else "⏾"
    elif "partly cloudy" in condition:
        return "🌥"
    elif "cloud" in condition or "overcast" in condition:
        return "☁"
    elif "rain" in condition or "drizzle" in condition:
        return "🌧"
    elif "thunder" in condition:
        return "⛈" if daytime else "🌩"
    elif "snow" in condition or "flurries" in condition:
        return "❄︎"
    elif "fog" in condition or "mist" in condition:
        return "🌫"
    else:
        return "❔"

# === GET WEATHER DATA ===
try:
    response = requests.get(URL, timeout=2)
    data = response.json()

    condition = data["current"]["condition"]["text"]
    temp_c = round(data["current"]["temp_c"])
    icon = getWeather(condition, isDay())

    print(f"{icon} {condition} {temp_c}°C")

except Exception as e:
    print("---")
