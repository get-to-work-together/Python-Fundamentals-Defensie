
filename = r'../Sandbox/ca-500.csv'

out = open('data_out.txt', 'w')

try:
    with open(filename) as f:

        headers = f.readline().strip().split(';')

        for regel in f:
            regel = regel.strip()

            fields = regel.split(';')

            d = dict(zip(headers, fields))

            if d['city'] == 'Montreal':
                print(d['first_name'], d['last_name'], d['city'], d['email'])

                out.write(regel + '\n')

except FileNotFoundError:
    print(f'Pech!!! Ik kan het bestand {filename} niet vinden.')

out.close()

