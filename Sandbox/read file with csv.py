import csv

filename = 'ca-500.csv'

with open(filename, 'r') as f:

    reader = csv.DictReader(f, delimiter = ';')
    for d in reader:

        if d['city'] in ('Montreal',):
            print(f"{d['first_name']:15} {d['last_name']:15} {d['email']:35} {d['city']}")
