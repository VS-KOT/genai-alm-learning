import requests

#current data {without date}
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


#range of date

def range_of_data(latitude,longitude,start_Date,end_Date):

    url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}"
    f"&longitude={longitude}"
    f"&hourly=temperature_2m"
    f"&start_date={start_Date}"
    f"&end_date={end_Date}"
    )
        
    response = requests.get(url)
    data = response.json()
    
    return data

