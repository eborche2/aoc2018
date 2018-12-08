from string import ascii_lowercase
with open('file.in') as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = content[0].split()
content = [int(x) for x in content]

def getName(names):
    row = 1
    while True:
        for each in ascii_lowercase:
            check = ""
            for x in range(row):
                check += each.upper()
            if check not in names:
                return check
        row += 1
headers = {}
metadata = 0
depth = []



def step(location):
    current = getName(headers)
    headers[current] = [content[location], content[location + 1]]
    depth.append(current)
    return location + 2


def endStep(location, metadata):
    endNode = depth.pop()

    for x in range(headers[endNode][1]):

        metadata += content[location]
        location += 1

    headers.pop(endNode)
    return location, metadata

loc = 0
flip = True

while True:
    if depth:
        if flip:
            headers[depth[-1]][0] -= 1
            flip = True

        if headers[depth[-1]][0] <= 0:
            loc, metadata = endStep(loc, metadata)
            flip = True
        else:
            loc = step(loc)
            flip = False
    else:
        flip = False
        loc = step(loc)
    if loc >= len(content):
        break

print(metadata) # part 1, note if you don't pop the headers this takes a very long time....



