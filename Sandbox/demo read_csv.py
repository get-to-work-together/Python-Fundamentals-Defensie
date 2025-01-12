import pandas as pd

df  = pd.read_csv('ca-500.csv', sep=';', decimal=',')

selection = df[df['city']=='Montreal']

print(selection[['first_name', 'last_name', 'city']])
