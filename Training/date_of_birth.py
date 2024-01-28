import datetime

user_input = input('Wat is jouw geboortedatum? [bv. 31-12-1967]: ')

date_of_birth = datetime.datetime.strptime(user_input, '%d-%m-%Y')
print(date_of_birth)

today = datetime.datetime.today()

days_alive = (today - date_of_birth).days

day_born = date_of_birth.strftime('%A')

print(f'Je bent al {days_alive} dagen op aarde.')
print(f'Je bent op een {day_born} geboren.')

