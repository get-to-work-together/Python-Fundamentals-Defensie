import requests
from datetime import datetime

city = input("Give city: ")

# openwheathermap api
url  = "http://api.openweathermap.org/data/2.5/forecast/daily"
url += "?appid=d1526a9039658a6f76950cff21823aff"
url += "&units=metric"
url += "&mode=json"
url += "&lang=nl"
url += "&cnt=14"
url += "&q=" + city

print(url)

try:
    response = requests.get(url)

except Exception as err:
    print("Cannot connect to " + url)
    print(err)

else:
    if (response.status_code == 200):

        body = response.text

        print(body)

        decoded = response.json()

        for day in decoded['list']:
            dt = datetime.fromtimestamp(day['dt'])
            temp_day = day['temp']['day']
            temp_night = day['temp']['night']
            weather = day['weather'][0]['description']

            print(f'{dt.strftime("%A %d-%m-%Y"):22} {temp_night:2.0f}° - {temp_day:2.0f}°   {weather}')

    elif response.status_code == 404:
        print("%s not found" % (city))

    else:
        print("error for city %s" % (city))


