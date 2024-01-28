
woorden = 'de timmerman timmert een kast in elkaar met zijn hamer'.split()


print(woorden)

print(sorted(woorden))

print(sorted(woorden, key = len))

def aantal_e(woord):
    return woord.count('e')

print(sorted(woorden, key = aantal_e))
print(sorted(woorden, key = aantal_e, reverse = True))

def aantal_m(woord):
    return woord.count('m')

print(sorted(woorden, key = aantal_m))
print(sorted(woorden, key = lambda woord: woord.count('m')))

print(sorted(woorden, key = lambda woord: woord.count('n')))

print(sorted(woorden, key = lambda woord: (woord[-1], len(woord))))
