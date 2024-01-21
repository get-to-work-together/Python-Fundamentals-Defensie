import csv
import os
import sys
import re

filename = '../Sandbox/ca-500x.csv'

try:
    with open(filename) as f:

        line = f.readline().rstrip('\n')
        headers = line.split(';')

        for line in f:
            line = line.rstrip('\n')
            values = line.split(';')

            d = dict(zip(headers, values))

            if re.search(r'\bh.*@aol.com', d['email']):

                print(f'{d["first_name"]:15} {d["last_name"]:15} {d["city"]:15} {d["email"]}')

except FileNotFoundError as ex:
    print('No file', filename)


# with open(filename, mode='r') as f:
#
#     headers = f.readline().strip().split(';')
#
#     for line in f:
#         values = line.strip().split(';')
#
#         d = dict(zip(headers, values))
#
#         if d['city'] in ('Montreal', ):
#             print(f"{d['first_name']:15} {d['last_name']:15} {d['city']:25} {d['email']:35}")








# import csv
#
# with open(filename, 'r') as f:
#     reader = csv.DictReader(f, delimiter=';')
#
#     for d in reader:
#
#         if d['city'] in ('Montreal', 'Toronto'):
#             print(f"{d['first_name']:15} {d['last_name']:15} {d['city']:25} {d['email']:35}")
