import copy
from string import ascii_lowercase
with open('file.in') as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = content[0]
loop = True
def shorter(polymer, start):
    try:
        if polymer[start] != polymer[start+1]:
            if polymer[start].lower() == polymer[start+1].lower():
                polymer = polymer[:start] + polymer[start+2:]
                if start == 0:
                    polymer = shorter(polymer, start)
                else:
                    polymer = shorter(polymer, start -1)

        return polymer
    except:
        return polymer
polymer = copy.copy(content)
while loop:

    size = len(polymer)
    for x in range(size):
        if x == size -2:
            break
        polymer = shorter(polymer, x)
    if len(polymer) == size:
        loop = False

print(len(polymer))#Solution 1(First solution took 45 seconds, so I refactored it to be much faster
winner = 50000
for each in ascii_lowercase:
    newPolymer = polymer.replace(each, '')
    newPolymer = newPolymer.replace(each.upper(), '')
    loop = True
    while loop:
        size = len(newPolymer)
        for x in range(size):
            if x == size-2:
                break
            newPolymer = shorter(newPolymer, x)
        if len(newPolymer) == size:
            loop = False
    if len(newPolymer) < winner:
        winner = len(newPolymer)
print(winner)# Solution 2 This was fun....
