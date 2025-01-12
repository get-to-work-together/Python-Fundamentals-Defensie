import re

filename = 'ca-500.csv'

with open(filename, 'r') as f:
    headers = f.readline().strip().split(';')

    for line in f:
        values = line.strip().split(';')

        d = dict(zip(headers, values))

        # if d['city'] in ('Montreal',):
        #     print(f"{d['first_name']:15} {d['last_name']:15} {d['email']:35} {d['city']}")

        if re.search(r'\bM.*l', d['city']):
            print(f"{d['first_name']:15} {d['last_name']:15} {d['email']:35} {d['city']}")
