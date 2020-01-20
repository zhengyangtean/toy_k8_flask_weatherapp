from flask import Flask
from flask import request
import socket
import requests    


app = Flask(__name__)

@app.route('/hello')
def helloIndex():
    return 'Hello World from Python Flask!'

@app.route('/whoami')
def whoami():
    hostname = socket.gethostname() 
    IPAddr = socket.gethostbyname(hostname)  
    return "I am " + hostname + " " + IPAddr

@app.route('/weather-list')
def weatherList():
    r = requests.get('https://api.data.gov.sg/v1/environment/2-hour-weather-forecast')
    weatherdata = r.json()
    areas = []
    for area in weatherdata["area_metadata"]:
        areas.append(area["name"])
    return str(areas)

@app.route('/weather')
def my_route():
    queryArea = request.args.get('area', default = "Ang Mo Kio", type = str)
    r = requests.get('https://api.data.gov.sg/v1/environment/2-hour-weather-forecast')
    weatherdata = r.json()
    areas = []
    for area in weatherdata["items"][0]["forecasts"]:
        if area["area"].lower() == queryArea.lower():
            return area
    return "Invalid Area"

app.run(host='0.0.0.0', port= 5000)
