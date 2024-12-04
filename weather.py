from dotenv import load_dotenv
from pprint import pprint
import os
import requests

load_dotenv()

def current_weather(city='Kansas City'):
    api_request_url = f'http://api.openweathermap.org/data/3.0/weather?appid={os.getenv("API_KEY")}&q={city}&units=standard'

    weather_data=requests.get(api_request_url).json()

    return weather_data

if __name__=='__main__ ':
    print('\n*** Get Current Weather Conditions ***\n')

    city=input("Enter city name to check weather")

    weather_response = current_weather(city)

    print('\n')
    print(weather_response)