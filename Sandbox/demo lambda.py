s = 'abacadabra'


def aantal_a(s):
    return s.count('a')

f = lambda s: s.count('a')

print(aantal_a(s))
print(f(s))

print(aantal_a)
print(lambda s: s.count('a'))

woorden = 'arend aap amandel abacadrbra vat'.split()

print( woorden )
print( sorted(woorden) )
print( sorted(woorden, key = len) )
print( sorted(woorden, key = aantal_a) )
print( sorted(woorden, key = lambda s: s.count('a')) )

print( list(filter(lambda s: s.count('a') >= 2, woorden)) )

print( [s for s in woorden if s.count('a') >= 2] )

print( list(map(lambda s: s[:3].upper(), woorden)) )

print( [s[:3].upper() for s in woorden] )


print( (s[:3].upper() for s in woorden) )
print( list((s[:3].upper() for s in woorden)) )
print( s[:3].upper() for s in woorden )
print( list(s[:3].upper() for s in woorden) )
