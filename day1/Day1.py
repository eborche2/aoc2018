
with open('file1.in') as f:
    content = f.readlines()
start = 0
content = [x.strip() for x in content]
found = list()
for each in content:
    start = start + int(each)
    found.append(start)
print(start) #part 1
notfound = True
beginning = 0
found = set(found)#Sets are supposedly faster for "in" checks
while notfound:
    if beginning == len(content):
        beginning = 0
    start = start + int(content[beginning])
    beginning += 1
    if start in found:
        notfound = False
print(start) #Part 2 (Note, run it a few times and look at the pattern and you will see why I only check the first list)
