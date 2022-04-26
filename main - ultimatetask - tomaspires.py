from http.client import responses
import json
import requests
import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# `https://samples.openweathermap.org/data/2.5/forecast?q=${city}&appid=01f15c9dedb7e8703045ad674a8c501d`

@app.route('/', methods=['GET'])
def home():
    return "Amazing API"

@app.route('/country', methods=['GET'])
def init():
    country_url = "https://restcountries.com/v3.1/name/"
    final_result = {}

    try:
        country_name = request.args.get('name')
        print(country_name)

        if country_name:
            try:
                complete_url = country_url+country_name
                response = requests.get(complete_url).json()
                capitals = []
                for item in response:
                    capital = item['capital']
                    for city in capital:
                        capitals.append(city)
                
                # check weather
                try:
                    for capital in capitals:
                        print('Vou buscar o tempo')
                        weather_response=requests.get(f'https://samples.openweathermap.org/data/2.5/forecast?q=${capital}&appid=01f15c9dedb7e8703045ad674a8c501d').json()
                        for item in weather_response['list']:
                            weather = item['weather'][0]['description']
                            break
                    final_result[capital] = weather
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
        return final_result
    except Exception as e:
        print(e)

app.run()
