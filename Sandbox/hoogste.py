def hoogste(*x):
    result_hoog = sorted(x)[-1]
    result_laag = sorted(x)[0]
    return result_laag, result_hoog

print(hoogste(1, 7))
print(hoogste(7, 52))

print(hoogste(1, 7, 5))
print(hoogste(12, 7, 78))
print(hoogste(7, 7, 2))

print(hoogste(7, 7, 2, 12))


t = hoogste(7, 7, 2, 12)
print('hoogste', t[1])


laag, hoog = hoogste(7, 7, 2, 12)
print('hoogste', hoog)
