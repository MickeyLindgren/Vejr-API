import requests
import json

api_key = '40636e008b70d01999d03d389ac2a218'

By = input('By: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={By}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp'] - 273.15
    desc = data['weather'][0]['description']
    print(f'Temperatur: {temp:.2f} Celsius')
    print(f'Beskrivelse: {desc}')
else:
    print('Fejl ved hentning af vejrdata')    