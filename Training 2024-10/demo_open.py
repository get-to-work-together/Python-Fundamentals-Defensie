import os

filename = 'data.txt'
filename_out = 'out.txt'

with open(filename) as f:
    with open(filename_out, mode='a') as f_out:

        header_line = f.readline()
        headers = header_line.rstrip('\n').split(',')
        print(headers)

        for line in f:
            line = line.rstrip('\n')
            columns = line.split(',')

            d = dict(zip(headers, columns))
            print(d)

            if int(d['aantal']) > 100:
                print(d['ID'])
                print(d, file=f_out)