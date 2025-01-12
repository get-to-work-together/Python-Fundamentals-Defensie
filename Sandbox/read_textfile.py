import re
import sys
import os

filename = 'textfile.txt'

if not os.path.exists(filename):
    print('Cannot find file %s.' % filename)
    sys.exit()

pattern = r'(\w+@\w+\.\w{2,3})'

email_addresses = []
try:
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            m = re.findall(pattern, line)
            email_addresses.extend(m)

    with open('email_addresses.txt', 'w') as f:
        for email_address in email_addresses:
            f.write(email_address + '\n')

except:
    print('Something went wrong' % filename)
    sys.exit()
            
