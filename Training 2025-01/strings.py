s = input('Geef tekst: ')

print('Originele tekst: ', s)
print('upper: ', s.lower())
print('lower: ', s.upper())
print('capitalize: ', s.capitalize())
print('title: ', s.title())
print('first 3 characters: ', s[:3])
print('ends with ?: ', s.endswith('?'))
print('ends with ?: ', s[-1] == '?')

print('snake case: ', s.lower().replace(' ', '_'))
