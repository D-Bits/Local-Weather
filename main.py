from current_weather import get_current_datetime, imperial_current_weather, metric_current_weather


if __name__ == "__main__":

    get_current_datetime()
    units = int(input('Please enter 1 for metric units, or 2 for imperial units: '))
    
    print() # Blank line for readability

    # If user enters 1, show weather data in metric. If 2, use imperial units
    if units == 1:
        metric_current_weather()
    elif units == 2:
        imperial_current_weather()
    else:
        raise Exception("Please enter only 1 or 2.")
    