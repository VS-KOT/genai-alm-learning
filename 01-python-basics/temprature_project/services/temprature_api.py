import requests

def get_weather(latitude, longitude):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m,wind_speed_10m"
    )

    response = requests.get(url)
    data = response.json()

    return {
        "temperature": data["current"]["temperature_2m"],
        "wind_speed": data["current"]["wind_speed_10m"]
    }
