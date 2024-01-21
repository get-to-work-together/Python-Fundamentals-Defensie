filename = 'demo.txt'

with open(filename, mode = 'a') as f:

    f.write('Line 1: abcd\n')
    f.write('Line 2: ioetuoe\n')
    f.write('Line 3: xyz\n')

    print('Line 4: with print function', file = f)
