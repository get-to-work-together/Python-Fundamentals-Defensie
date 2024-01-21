#!/usr/bin/python
import random
import string

def give_lower(exclude = 'l'):
    return random.choice([c for c in string.ascii_lowercase if c not in exclude])

def give_upper(exclude = 'IO'):
    return random.choice([c for c in string.ascii_uppercase if c not in exclude])

def give_number():
    return random.choice(string.digits)

def give_char(exclude = '\\\'"'):
    return random.choice([c for c in string.punctuation if c not in exclude])

def give_any():
    options = ['lower', 'upper', 'number', 'char']
    pick = random.choice(options)
    if pick == "lower":
        return give_lower()
    if pick == "upper":
        return give_upper()
    if pick == "number":
        return give_number()
    if pick == "char":
        return give_char()
        
        
while True:
    length = int(input("Voer de lengte in: "))
    if 0 <= length < 8:
        print("unsafe password length, to short")
    if 8 <= length <= 20:
        break
    else:
        print("Password too long, impossible to remember")

# Start with required characters
password = [give_lower(), give_upper(), give_number(), give_char()]

# Substract the required lower, upper, number and char
for _ in range(length - len(password)):
    password.append(give_any())

random.shuffle(password)
password = ''.join(password)

print(password)