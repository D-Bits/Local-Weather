import requests, os, time, datetime
from datetime import datetime


# Get the current day and time
def get_current_datetime():

    now = datetime.now()
    # Print the current date and time
    print()
    print("Current Date & Time: ")
    print(now.month, "-", now.day, "-", now.year)
    print(now.hour, ":", now.minute)
    print()
    print()

def current_weather():

    # Define the GET request to the API
    # Get current weather data from Seattle

    # Old, parameterized attempt
    """
    # api_key = os.getenv('WEATHER_API_KEY')
    # api_url = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params={'q': 'Seattle,us', 'APPID': api_key, 'units': 'imperial'})
    """
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q=Seattle,us&APPID=ffc5321958cd581c26b5965c4947ac9f&units=imperial'
    response = requests.get(api_url)
    data = response.json()

    temp = data['main']['temp']
    ws = data['wind']['speed']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']


    print("The current weather for Seattle is: ")
    print() # Blank line for readability

    print("The current temp is:", temp, "degrees") 
    print()

    print("Wind Speed:", ws, "mph")
    print()

    print("Humidity:", humidity)
    print()

    print('Summary: ' + description)
    print()


# Get the 5-day forecast for Seattle
def five_day():

    api_key = os.environ.get()
    five_day_url = f'https://api.openweathermap.org/data/2.5/forecast?q=Seattle,us&APPID={api_key}&units=imperial'
    response = requests.get(five_day_url)
    data = response.json()

    print(data)



if __name__ == "__main__":

    get_current_datetime()
    current_weather()
    # five_day()
