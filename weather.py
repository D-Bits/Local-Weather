import requests, os


def current_weather():

    # Define the GET request to the API
    # Get current weather data from Seattle

    # Old attempts
    """
    # api_key = os.getenv('WEATHER_API_KEY')
    # api_url = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params={'q': 'Seattle,us', 'APPID': api_key, 'units': 'imperial'})
    """
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q=Seattle,us&APPID=ffc5321958cd581c26b5965c4947ac9f&units=imperial'
    response = requests.get(api_url)
    data = response.json()

    temp = data['main']['temp']
    ws = data['wind']['speed']
    description = data['weather'][0]['description']

    print()
    print("The current weather for Seattle is: ")
    print() # Blank line for readability

    print("The current temp is: ") 
    print(temp)
    print()

    print("Wind Speed: ")
    print(ws)
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


def main():

    current_weather()
    # five_day()


main()