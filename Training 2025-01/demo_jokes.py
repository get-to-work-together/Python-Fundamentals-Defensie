import requests

from pprint import pprint
import random
import time


url = 'https://api.sampleapis.com/jokes/goodJokes'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    joke = random.choice(data)

    print(joke['setup'])
    time.sleep(5)
    print(joke['punchline'])

else:
    print('Could not open site.')