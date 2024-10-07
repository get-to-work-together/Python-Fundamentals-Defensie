
# counter = 0
# while counter < 10:
#     print(counter)
#     counter += 1



# magic_number = 14
# for getal in range(1, 21):
#     if getal == magic_number:
#         continue
#     print(getal)


while True:
    number = int(input('Enter an number between 1 and 10: '))
    if 1 <= number <= 10:
        break

print('The number is %d' % number)
