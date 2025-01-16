import requests

import json

city = input('Geef stad: ')

url = 'http://api.openweathermap.org/data/2.5/weather?appid=d1526a9039658a6f76950cff21823aff&units=metric&mode=json&lang=nl&q=' + city

response = requests.get(url)

print(response.status_code)

r = response.text

d = json.loads(r)

print(d)

temperature = d['main']['temp']

print(f'Het is nu {temperature} in {city}')


