import os, time, requests
from datetime import datetime
from requests import get


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
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q=Seattle,us&APPID=ffc5321958cd581c26b5965c4947ac9f&units=imperial'
    response = requests.get(api_url)
    data = response.json()

    temp = data['main']['temp']
    ws = data['wind']['speed']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']


    print("The current (imperial) weather for Seattle is: ")
    print() # Blank line for readability

    print("The current temp is:", temp, "degrees") 
    print()

    print("Wind Speed:", ws, "mph")
    print()

    print("Humidity:", humidity)
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


    print("The current (metric) weather for Seattle is: ")
    print() # Blank line for readability

    print("The current temp is:", temp, "degrees") 
    print()

    print("Wind Speed:", ws, "kph")
    print()

    print("Humidity:", humidity,"%")
    print()

    print('Summary:', description)
    print()


if __name__ == "__main__":

    get_current_datetime()
    units = int(input('Please enter 1 for metric weather, or 2 for imperial units: '))
    
    print() # Blank line for readability

    # If user enters 1, show weather data in metric. If 2, use imperial units
    if units == 1:
        metric_current_weather()
    elif units == 2:
        imperial_current_weather()
    else:
        raise Exception("Please enter 1 or 2.")
    
