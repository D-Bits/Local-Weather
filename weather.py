import requests


def current_weather():

    # Define the GET request to the API
    # Get current weather data from Seattle
    current_weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=Seattle,us&APPID=ffc5321958cd581c26b5965c4947ac9f&units=imperial'
    response = requests.get(current_weather_url)
    data = response.json()

    temp = data['main']['temp']
    ws = data['wind']['speed']
    description = data['weather'][0]['description']

    print()
    print("The current weather for Seattle is: ")
    print() # Blank line for readability

    print('Temperature: {}'.format(temp) + " degrees")
    print('Wind Speed: {}'.format(ws) + " mph")
    print('Summary: {}'.format(description))
    print()

# Get the 5-day forecast for Seattle
def five_day():

    five_day_url = 'http://api.openweathermap.org/data/2.5/forecast?q=Seattle,us&APPID=ffc5321958cd581c26b5965c4947ac9f&units=imperial'
    response = requests.get(five_day_url)
    data = response.json()

    print(data)


def main():

    current_weather()
    # five_day()


main()