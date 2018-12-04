from datetime import datetime
from operator import itemgetter


def getNewDict():
    newDict = {}
    for x in range(60):
        newDict[x] = 0
    return newDict


def addToGuard(guard, guards, start, stop):
    for x in range(start, stop):
        guards[guard][x] += 1


with open('file.in') as f:
    content = f.readlines()
content = [x.strip() for x in content]
matrix = matrix = [["." for i in range(2)] for i in range(len(content))]
for i, timestamp in enumerate(content):
    matrix[i][0] = datetime.strptime(timestamp[1:17], '%Y-%m-%d %H:%M')
    matrix[i][1] = timestamp[18:]
matrix = sorted(matrix, key=itemgetter(0))
guards = {}
start = 0
stop = 0
flip = False
guard = None
for stamp in matrix:
    if "Guard" in stamp[1]:
        guard = int(stamp[1][stamp[1].find('#')+1:stamp[1].find('b')])
        if guard not in guards:
            guards[guard] = getNewDict()
        if flip:
            import pdb; pdb.set_trace()
    elif "falls" in stamp[1]:
        start = stamp[0].minute
    elif "wakes" in stamp[1]:
        stop = stamp[0].minute
        flip = True
    if flip:
        addToGuard(guard, guards, start, stop)
        flip = False
winner = [0, 0, 0]
for each in guards:
    minutes = 0
    cMax = 0
    total = 0
    for minute in guards[each]:
        total += guards[each][minute]
        if guards[each][minute] > cMax:
            cMax = guards[each][minute]
            minutes = minute
    if total > winner[2]:
        winner[0] = each
        winner[1] = minutes
        winner[2] = total
print(winner[0] * winner[1])# part 1
winner = [0, 0, 0]
for each in guards:
    minutes = 0
    cMax = 0
    total = 0
    for minute in guards[each]:
        total += guards[each][minute]
        if guards[each][minute] > cMax:
            cMax = guards[each][minute]
            minutes = minute
    if cMax > winner[1]:
        winner[0] = each
        winner[1] = cMax
        winner[2] = minutes
print(winner[0] * winner[2])# part 2






