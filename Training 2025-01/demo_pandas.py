import pandas as pd
import matplotlib.pyplot as plt

# From CBS: https://www.cbs.nl/en-gb/visualisations/dashboard-population/population-counter
filename = 'Population.csv'

df = pd.read_csv(filename, sep=';', decimal=',', index_col='Year')

df['Population'] = df['Population'] * 1000000

print(df)

df.plot()

plt.grid()
plt.show()
