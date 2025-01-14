year = int(input('Geef een jaar: '))

is_leapyear = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(year, is_leapyear)



deelbaar_door_4 = year % 4 == 0
deelbaar_door_100 = year % 100 == 0
deelbaar_door_400 = year % 400 == 0
is_leapyear = deelbaar_door_4 and not deelbaar_door_100 or deelbaar_door_400

import calendar
is_leapyear = calendar.isleap(year)

if is_leapyear:
    print(year, 'is een schrikkeljaar')
else:
    print(year, 'is een NIET schrikkeljaar')