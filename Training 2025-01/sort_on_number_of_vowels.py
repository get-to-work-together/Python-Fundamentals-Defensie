s = 'het is toch wonderlijk dat er zoveel verschillende mogelijkheden zijn om iets goed te doen'

woorden = s.split()

print(sorted(woorden, key = lambda w: sum(w.lower().count(v) for v in 'aeiou')))
