import csv
import pandas as pd

filename = 'ca-500.csv'


with open(filename) as f:
    reader = csv.DictReader(f, delimiter = ';')
    for d in reader:
        if d['city'] == 'Montreal':
            print(d['first_name'], d['last_name'], d['city'])



df = pd.read_csv(filename, sep = ';')

print( df.loc[df['city']=='Montreal', ['first_name','last_name','city']] )
