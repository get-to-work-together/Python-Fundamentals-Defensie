magicnumber = int(input("Choose a magic number: "))

print("\nThis loop terminates if it hits the magic number")
for i in range(1, 21):
    if i == magicnumber:
        break
    print(i)

print("\nThis loop skips the magic number")
for i in range(1, 21):
    if i == magicnumber:
        continue
    print(i)
