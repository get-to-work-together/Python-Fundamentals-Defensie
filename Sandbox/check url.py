import requests

class InvalidConnectionException(Exception):
    pass


url = 'https://nu.nl?q=x'

try:
    r = requests.get(url)

    if r.status_code == 200:
        print(r)

    else:
        raise InvalidConnectionException(f'Status code in not 200. It is {r.status_code }')

except InvalidConnectionException as ex:
    print(f'Kan niet verbinden met {url}.', ex)