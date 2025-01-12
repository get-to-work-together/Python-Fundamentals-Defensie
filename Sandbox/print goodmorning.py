def print_goodmorning(naam, n = 1):
    n = min(n, 10)
    for _ in range(n):
        print(f'Goodmorning {naam}')
    print('How are you today?')
    print('Have a great day!')

# ----------------------------------------------------------

print_goodmorning('Peter')
print_goodmorning('Willie', 5)

def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    return bmi

def som_en_product(x1, x2, x3, offset = 0):
    som = offset + x1 + x2 + x3
    product = offset + x1 * x2 * x3
    return som, product

offset = 100
print( som_en_product(1, 5, 9, offset) )
print(offset)