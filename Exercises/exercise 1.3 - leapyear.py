
year = int(input('Give a year: '))

is_leapyear = ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0)

print(year, is_leapyear)












if is_leapyear:
    print(f'Year {year} is a leapyear')
else:
    print(f'Year {year} is NOT a leapyear')

print('Really!')
















# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             is_leapyear = True
#         else:
#             is_leapyear = False
#     else:
#         is_leapyear = True
# else:
#     is_leapyear = False
#
# print(year, is_leapyear)






# divisible_by_4 = year % 4 == 0
# divisible_by_100 = year % 100 == 0
# divisible_by_400 = year % 400 == 0
#
# is_leapyear = (divisible_by_4 and not divisible_by_100) or divisible_by_400








# import calendar
#
# if calendar.isleap(year):
#     print(f'{year} is a leapyear')
# else:
#     print(f'{year} is NOT a leapyear')
