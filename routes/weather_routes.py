from flask import Blueprint
import requests
import os

weather_bp = Blueprint(
    'weather',
    __name__
)

API_KEY="ec6f3a50fe2e3c1073903a460fb777b2"


@weather_bp.route('/weather')

def get_weather():

    city="Chennai"

    try:

        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response=requests.get(url)

        data=response.json()

        return {

            "City":city,

            "Temperature":
            data['main']['temp'],

            "Humidity":
            data['main']['humidity'],

            "Condition":
            data['weather'][0]['main'],

            "WindSpeed":
            data['wind']['speed']

        }

    except Exception as e:

        return {

            "status":"error",

            "message":str(e)

        }