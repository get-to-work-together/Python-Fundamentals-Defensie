import pandas as pd

areacodes =  {'Eindhoven':'040',
              'Amsterdam':'020',
              'Rotterdam':'010',
              'Groningen':'050',
              'Utrecht':'030'}

province =  {'Eindhoven':'NB',
              'Amsterdam':'NH',
              'Rotterdam':'ZH',
              'Groningen':'G',
              'Utrecht':'U'}

inhabitants =  {'Eindhoven':60000,
              'Amsterdam':200000,
              'Rotterdam':180000,
              'Groningen':90000,
              'Utrecht':70000}

df = pd.DataFrame({
    'areacode': areacodes,
    'province': province,
    'inhabitants': inhabitants
})

df1 = df[df['inhabitants']>=100000]

df['location'] = df.index + ', ' + df['province']

print(df.sort_values('areacode'))