t = input('Give me some text please: ')

print('Original:', t)

print('Number of characters:', len(t))

print('Upper:', t.upper())
print('Lower:', t.lower())
print('Capitalize:', t.capitalize())
print('Title:', t.title())

print('First three characters:', t[:3])

print('Ends with a ?:', t.endswith('?'))
print('Ends with a ?:', t[-1] == '?')

print('Snake case:', t.lower().replace(' ', '_'))

print('Pascal case:', t.title().replace(' ', ''))
print('Camel case:', t[0].lower() + t.title().replace(' ', '')[1:])
print('Screaming case:', t.upper().replace(' ', '_'))
