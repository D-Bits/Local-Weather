import os, time, requests
from datetime import datetime
from requests import get


# Prompt the user to enter a city
city = input('Please enter a city: ')

# Get the current day and time
def get_current_datetime():

    # Define current datetime
    now = datetime.now()

    # Print the current date and time
    print()
    print("Current Date & Time: ", now)
    print()
    print()


# Define the GET request to the API
def imperial_current_weather():

    # Old, parameterized attempt
    """
    # api_key = os.getenv('WEATHER_API_KEY')
    # api_url = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params={'q': 'Seattle,us', 'APPID': api_key, 'units': 'imperial'})
    """
    # Get current weather data from Seattle
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city},us&APPID=ffc5321958cd581c26b5965c4947ac9f&units=imperial'
    response = requests.get(api_url)
    data = response.json()

    temp = data['main']['temp']
    ws = data['wind']['speed']
    humidity = data['main']['humidity']
    sunrise = data['sys']['sunrise']
    description = data['weather'][0]['description']


    print(f"The current (imperial) weather for {city} is: ")
    print() # Blank line for readability

    print("The current temp is:", temp, "degrees") 
    print()

    print("Wind Speed:", ws, "mph")
    print()
    
    print("Humidity:", humidity,"%")
    print()

    print('Summary:', description)
    print()
    print()


def metric_current_weather():

    # Get current weather data from Seattle
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q=Seattle,us&APPID=ffc5321958cd581c26b5965c4947ac9f&units=metric'
    response = requests.get(api_url)
    data = response.json()

    temp = data['main']['temp']
    ws = data['wind']['speed']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']


    print(f"The current (metric) weather for {city} is: ")
    print() # Blank line for readability

    print("The current temp is:", temp, "degrees") 
    print()

    print("Wind Speed:", ws, "kph")
    print()

    print("Humidity:", humidity,"%")
    print()

    print('Summary:', description)
    print()
    
