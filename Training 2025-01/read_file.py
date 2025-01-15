filename_in = 'namen.txt'
filename_out = 'out.txt'

with open(filename_in, mode = 'r') as f_in:
    with open(filename_out, mode='w') as f_out:
        for line in f_in:
            line = line.strip()
            if line.lower().startswith('m'):
                print(line, file = f_out)
