

def minimum_maximum(*getallen):
    hoogste = getallen[0]
    laagste = getallen[0]
    for getal in getallen[1:]:
        if getal > hoogste:
            hoogste = getal
        if getal < laagste:
            laagste = getal
    return laagste, hoogste

#-----------

if __name__ == '__main__':

    print(minimum_maximum(34, 66, 45, 99))