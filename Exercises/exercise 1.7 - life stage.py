# Exercise 5.6 from Crash Course for Python

age = int(input('What age? : '))

if age < 2:
    print('A baby')

elif age < 4:
    print('A toddler')

elif 4 <= age < 13:
    print('A kid')

elif age >= 13 and age < 20:
    print('A teenager')

elif age in range(20, 65):
    print('An adult')

else:
    print('An elder')






# match age:
#     case age if age < 2:
#         print('A baby')

#     case age if 2 <= age < 4:
#         print('A toddler')

#     case age if 4 <= age < 13:
#         print('A kid')

#     case age if 13 <= age and age < 20:
#         print('A teenager')

#     case age if 20 <= age < 65:
#         print('An adult')

#     case age if age >= 65:
#         print('An elder')

















# lijst = [{'bounds': [0, 2], 'stage': 'baby'},
#          {'bounds': [2, 4], 'stage': 'toddler'},
#          {'bounds': [4, 12], 'stage': 'kid'},
#          {'bounds': [13, 20], 'stage': 'teenager'},
#          {'bounds': [21, 65], 'stage': 'adult'},
#          {'bounds': [65, 110], 'stage': 'elder'}]
#
# for d in lijst:
#     lower, upper = d['bounds']
#     if lower <= age < upper:
#         print(d['stage'])
#         break






# d = {'baby': [0, 2],
#      'toddler': [2, 4],
#      'kid': [4, 12],
#      'teenager': [13, 20],
#      'adult': [21, 65],
#      'elder': [65, 110]}
#
# for stage, (lower, upper) in d.items():
#     if lower <= age < upper:
#         print(stage)
#         break
