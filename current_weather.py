import os, time, requests
from datetime import datetime
from requests import get


# Prompt the user to enter a city
print()
city = input('Please enter a city: ')

# Get the current day and time
def get_current_datetime():

    # Define current datetime
    now = datetime.now()

    # Print the current date and time
    print()
    print("Current Date & Time: ", now, '\n')


# Define the GET request to the API
def imperial_current_weather():

    api_key = os.getenv('WEATHER_API_KEY')
    # Old, parameterized attempt
  
    # Get current weather data from Seattle
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city},us&APPID={api_key}&units=imperial'
    response = requests.get(api_url)
    data = response.json()

    temp = data['main']['temp']
    ws = data['wind']['speed']
    humidity = data['main']['humidity']
    sunrise = data['sys']['sunrise']
    sunrise_formatted = datetime.fromtimestamp(sunrise / 1e3)
    sunset = data['sys']['sunset']
    sunset_formatted = datetime.fromtimestamp(sunset / 1e3)
    description = data['weather'][0]['description']


    print(f"The current weather for {city} is: \n")

    print("The current temp is:", temp, "degrees F. \n") 

    print("Wind Speed:", ws, "mph \n")
    
    print("Humidity:", humidity,"% \n")

    print('Sunrise at:', sunrise_formatted, '\n')

    print('Sunset at:', sunset_formatted, '\n')

    print('Summary:', description, '\n')


def metric_current_weather():

    # Get current weather data from Seattle
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q=Seattle,us&APPID=ffc5321958cd581c26b5965c4947ac9f&units=metric'
    response = requests.get(api_url)
    data = response.json()

    temp = data['main']['temp']
    ws = data['wind']['speed']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']


    print(f"The current weather for {city} is: \n")

    print("The current temp is:", temp, "degrees C \n") 

    print("Wind Speed:", ws, "kph \n")
  
    print("Humidity:", humidity,"% \n")

    print('Summary: ', description, '\n')
    
