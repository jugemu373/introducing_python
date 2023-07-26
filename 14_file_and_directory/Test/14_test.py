# 14.1
import os
with os.scandir('.') as it:
    entries = [entry.name for entry in it]

print(entries)


# 14.2
with os.scandir('..') as it:
    entries = [entry.name for entry in it]

print(entries)


# 14.3
test1 = 'This is a test of the emergency text system'
print(len(test1))

with open('test.txt', 'w') as outfile:
    outfile.write(test1)


# 14.4
with open('test.txt', 'r') as infile:
    test2 = infile.read()

print(test2)
print(len(test2))
print(test1 == test2)
