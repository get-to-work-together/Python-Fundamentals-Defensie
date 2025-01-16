import os

print(os.getcwd())

for item in sorted(os.listdir()):
    print(item)

os.chdir('..')
print(os.getcwd())
