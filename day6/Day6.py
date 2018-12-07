from string import ascii_lowercase
with open('file.in') as f:
    content = f.readlines()
content = [x.strip() for x in content]
key = {}
for i, each in enumerate(content):
    if i < 26:
        key[ascii_lowercase[i].upper()] = [int(each[:each.find(',')]), int(each[each.find(',')+1:])]
    else:
        key[ascii_lowercase[i - 26].upper() + ascii_lowercase[i -26].upper()] = [int(each[:each.find(',')]), int(each[each.find(',')+1:])]
matrix = [[0 for i in range(400)] for i in range(400)]
for each, value in key.items():
    matrix[value[0]][value[1]] = each
for i, each in enumerate(matrix):
    for j, row in enumerate(matrix[i]):
        values = []
        if matrix[i][j] == 0:
            for current, value in key.items():
                values.append([abs(value[0] - i) + abs(value[1] - j), current])
            values.sort()
            if values[0][0] == values[1][0]:
                matrix[i][j] = '. '
            else:
                if len(values[0][1]) == 1:
                    matrix[i][j] = values[0][1].lower()
                else:
                    matrix[i][j] = values[0][1].lower()
            del values
infinite = set()

for x in range(0, 400):
    infinite.add(matrix[x][0].upper())
    infinite.add(matrix[x][399].upper())
    infinite.add(matrix[0][x].upper())
    infinite.add(matrix[399][x].upper())
largest = 0
for each, value in key.items():
    if each not in infinite:
        rowcount = 0
        for count in matrix:
            rowcount += count.count(each.lower())
        if rowcount > largest:
            largest = rowcount

print(largest + 1)# It doesn't count itself, so you have to add the plus 1....

for i, each in enumerate(matrix):
    for j, row in enumerate(matrix[i]):
        values = []

        for current, value in key.items():
            values.append([abs(value[0] - i) + abs(value[1] - j), current])
        values.sort()
        total = 0
        for val in values:
            total +=val[0]
        if total < 10000:
            matrix[i][j] = '#'

        del values
count = 0
for counting in matrix:
    count += counting.count('#')
print(count)# Part two , takes almost a minute to do it this way...



