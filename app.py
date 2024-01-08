import config

from flask import Flask, render_template
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

    # Set desired API call information
    address = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial'.format(lat=LATITUDE, lon=LONGITUDE, api_key=API_KEY)

    response = requests.get(address)

    temperature = parse_temperature(response.json())

    return render_template("sf_temp.html", temperature=temperature, location=LOCATION)

@app.route("/borrego-springs")
def borrego_springs_temperature():
    # Set latitude and longitude of San Francisco
    LATITUDE = '33.255871'
    LONGITUDE = '-116.375015'
    LOCATION = 'Borrego Springs'

    # Set desired API call information
    address = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial'.format(lat=LATITUDE, lon=LONGITUDE, api_key=API_KEY)

    response = requests.get(address)

    temperature = parse_temperature(response.json())

    return render_template("borrego_temp.html", temperature=temperature, location=LOCATION)

def parse_temperature(response):
    temperature = str(response['main']['temp'])
    return temperature

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)