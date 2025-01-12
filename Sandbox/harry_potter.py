filename = 'Book1.txt'
filename_out = 'lines.txt'

with open(filename, encoding = 'utf8', mode='r') as f:
    with open(filename_out, mode='w') as f_out:
        for linenr, line in enumerate(f, start=1):
            line = line.rstrip('\n')
            if 'Hermione' in line:
                print(linenr, line)
                # f_out.write(f'{linenr}: {line}\n')
                print(linenr, line, file = f_out)

