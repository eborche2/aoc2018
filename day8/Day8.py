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
used_nodes = []
final_values = {}
final_nodes = {}
header_copy = {}

def getNode(location):
    for x in range(1, len(content)):
        if location + str(x) not in used_nodes:
            used_nodes.append(location+str(x))
            return location + str(x)


def step(location):
    current = getName(headers)
    child_node = None
    if not depth:
        headers[current] = [content[location], content[location + 1], None, []]
        header_copy[current] = content[location]
    else:
        header_copy[current] = content[location]
        child_node = getNode(depth[-1])
        headers[current] = [content[location], content[location + 1], child_node, []]
    depth.append(current)
    if child_node:
        final_nodes[child_node] = current
    return location + 2


def endStep(location, metadata):
    endNode = depth.pop()
    for x in range(headers[endNode][1]):
        headers[endNode][3].append(content[location])
        metadata += content[location]
        location += 1

    #headers.pop(endNode)
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

print(metadata) # part 1, note if you don't pop the headers this takes longer... Need headers for part 2


def find_final(letter, final_count):
    if header_copy[letter] != 0:
        for each in headers[letter][3]:
            try:
                final_count = find_final(final_nodes[letter+str(each)], final_count)
            except:
                pass
        return final_count
    else:
        count = 0
        for each in headers[letter][3]:
            count += each
        return final_count + count


final = find_final('A', 0)
print(final) #Bah, part 2 took me longer than it should have....



