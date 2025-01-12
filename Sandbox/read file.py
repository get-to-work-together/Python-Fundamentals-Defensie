

# filename = 'C:/Users/peter/Computrain/_InCompany/Defensie/Python Fundamentals/Sandbox/data.txt'
# Windows:
# filename = r'C:\Users\peter\Computrain\_InCompany\Defensie\Python Fundamentals\Sandbox\data.txt'
# filename = 'C:\\Users\\peter\\Computrain\\_InCompany\\Defensie\\Python Fundamentals\\Sandbox\\data.txt'


# f = open(filename)
# content = f.read()
# f.close()

filename= 'demo.txt'

with open(filename, mode = 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        print(line)

with open(filename, mode = 'r') as f:
    print(f.read())