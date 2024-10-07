import pandas

filename = 'ca-500.csv'

df = pandas.read_csv(filename, sep=';', dayfirst=True)

print(df[['first_name','last_name']])