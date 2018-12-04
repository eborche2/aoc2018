
with open('file.in') as f:
    content = f.readlines()
content = [x.strip() for x in content]
matrix = [[0 for i in range(1000)] for i in range(1000)]
for square in content:
    start = square.find('@') + 1
    middle = square.find(',')
    end = square.find(':')
    dimension = square.find('x')
    x = int(square[start:middle])
    y = int(square[middle + 1:end])
    w = int(square[end + 1:dimension])
    h = int(square[dimension +1:])
    for z in range(x , x + w):
        for g in range(y , y  + h):
            if matrix[z][g] != 0:
                matrix[z][g] = -1
            else:
                matrix[z][g] = square[1:start -1]
total = 0
for each in matrix:
    total += each.count(-1)
print(total) #part 1

for square in content:
    start = square.find('@') + 1
    middle = square.find(',')
    end = square.find(':')
    dimension = square.find('x')
    x = int(square[start:middle])
    y = int(square[middle + 1:end])
    w = int(square[end + 1:dimension])
    h = int(square[dimension +1:])
    noOverlap = True
    for z in range(x , x + w):
        for g in range(y , y  + h):
            if matrix[z][g] == -1:
                noOverlap = False
                break
        if not noOverlap:
            break
    if noOverlap:
        print(square[1:start -1]) #part 2
