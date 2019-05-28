"""
WORK IN PROGRESS. NOT YET WORKING.
"""

import requests, os


# Get the 5-day forecast for Seattle
def five_day():

    api_key = os.environ.get()
    five_day_url = f'https://api.openweathermap.org/data/2.5/forecast?q=Seattle,us&APPID={api_key}&units=imperial'
    response = requests.get(five_day_url)
    data = response.json()

    print(data)