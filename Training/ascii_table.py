for first_ascii in range(32, 128, 16):
    ascii_range = range(first_ascii, first_ascii + 16)
    ascii_row = ''.join(' %4d' % a for a in ascii_range)
    chr_row = ''.join('%5s' % chr(a) for a in ascii_range)
    print('ascii  ', ascii_row)
    print('chr    ', chr_row)
