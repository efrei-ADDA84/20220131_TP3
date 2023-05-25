import os
import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root(lat: float, lon: float):
    API_Key = os.environ.get('API_KEY')

    def get_weather(lat, lon):
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']
            temperature = data['main']['temp'] - 273.15 # Convert Kelvin to Celsius
            return f'The weather in your location is {weather} with a temperature of {temperature:.2f}°C'
        else:
            return 'Failed to retrieve weather data'

    return get_weather(lat, lon)