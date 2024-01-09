import config

from flask import Flask, render_template
from datetime import datetime
import requests
import json

app = Flask(__name__)
API_KEY = config.openweather_api_key

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/san-francisco")
def san_francisco_temperature():
    # Set latitude and longitude of San Francisco
    LATITUDE = '37.7898669'
    LONGITUDE = '-122.4268036'
    LOCATION = "San Francisco"

    temperature = get_temperature(LATITUDE, LONGITUDE)

    return render_template("sf_temp.html", temperature=temperature, location=LOCATION)

@app.route("/borrego-springs")
def borrego_springs_temperature():
    # Set latitude and longitude of San Francisco
    LATITUDE = '33.255871'
    LONGITUDE = '-116.375015'
    LOCATION = 'Borrego Springs'

    temperature = get_temperature(LATITUDE, LONGITUDE)

    return render_template("borrego_temp.html", temperature=temperature, location=LOCATION)

# TODO add main index page that displays all available routes (premade)
# TODO add a page that accepts a city name and then gives above info (name -> geochaching api for lat and long -> openweather api for temp)

@app.route("/testing")
def testing():
    time = datetime.now()
    time = time.strftime('%H:%M:%S')

    print('Tested at @ {time}'.format(time=time))
    coordinates = get_coordinates('Morgan_Hill,CA,US')
    return str(coordinates[0])+', '+str(coordinates[1])

def parse_coordinates(response):
    try:
        coordinates = []
        coordinates.append(str(response[0]['lat']))
        coordinates.append(str(response[0]['lon']))
        return coordinates
    except Exception as e:
        return str(e)

def get_coordinates(location):
    address = 'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={api_key}'.format(location=location, api_key=API_KEY)

    response = requests.get(address)
    coordinates = parse_coordinates(response.json())

    return coordinates

def parse_temperature(response):
    temperature = str(response['main']['temp'])
    return temperature

def get_temperature(latitude, longitude):
    """
    Returns the temperature in fahrenheit at a given coordinates (lat, lon)

    Args:
        latitude: string formatted latitude
        longitude: string formatted longitude
    
    Returns:
        temperature: string formatted temperature in fahrenheit
    """
    address = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial'.format(lat=latitude, lon=longitude, api_key=API_KEY)

    response = requests.get(address)

    temperature = parse_temperature(response.json())

    return temperature

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)