import os
print(os.getcwd())

filename = 'data.txt'
filename = r'/Users/peter/Computrain/_InCompany/Defensie/Python Fundamentals/Sandbox/data.txt'



# f = open(filename)
# content = f.read()
# f.close()


# with open(filename) as f:
#     content = f.read()
#
# print(content)


with open(filename) as f:
    for linenr, line in enumerate(f, start = 1):
        line = line.rstrip('\n')
        if 'o' in line:
            print(linenr, line)