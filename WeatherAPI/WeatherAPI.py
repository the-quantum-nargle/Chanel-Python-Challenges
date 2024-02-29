import requests
import os
from dotenv import load_dotenv

# Load environment variables, including the API key for OpenWeatherMap
load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')


# API endpoint configuration
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
UNITS = 'metric'  # Use 'metric' for Celsius, 'imperial' for Fahrenheit (default)


# Request weather data for a city provided by the user
CITY_NAME = input('Enter city name: ')
params = {
    'q': CITY_NAME,
    'appid': API_KEY,
    'units': UNITS
}
response = requests.get(BASE_URL, params=params)


if response.status_code == 200:
    # Process a successful response
    data = response.json()
    print(f"\nWeather in {CITY_NAME}:")
    print(f"Description: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']}m/s")

else:
    # Handle errors and attempt to extract the error message from the response
    error_data = response.json()
    error_message = error_data.get('message', 'No error message provided')
    print("Failed to retrieve weather data.")
    print(f"Error: {error_message}")
    