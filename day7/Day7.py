import collections
with open('file.in') as f:
    content = f.readlines()
content = [x.strip() for x in content]
key = {}
steps = {}
for each in content:
    pre = each[5:6]
    step = each[36:37]
    if step not in key:
        key[step] = False
    if pre not in key:
        key[pre] = False
    if pre not in steps:
        steps[pre] = []
    if step not in steps:
        steps[step] = []
    steps[step].append(pre)
steps = collections.OrderedDict(sorted(steps.items()))
key = collections.OrderedDict(sorted(key.items()))

for letter, found in steps.items():
    found.sort()


def findFirstLetter(letters, letter, current):
    if not letters:
        return letter
    for each in letters:
        if key[each] is False:
            check = findFirstLetter(steps[each], each, current)
            if check is None:
                check = each
            if current is None:
                current = check
            else:
                if current > check:
                    current = check
    return current


order = []
notFound = True
while notFound:
    current = None
    for letter, found in key.items():
        if not found:
            if not steps[letter]:
                check = letter
            else:
                check = findFirstLetter(steps[letter], letter, None)
            if check is None:
                check = letter
            if current is None:
                current = check
            elif current > check:
                current = check
    if current is None:
        notFound = False
    else:
        order.append(current)
        key[current] = True

print(''.join(order)) #Sweet little recursion, fast
for i, each in key.items():
    key[i] = False
x = 0
notEnd = True
workers = []
workers = [[None, None] for i in range(5)]

while notEnd:
    if x > 0:
        for each in workers:
            if each[1]:
                each[1] -= 1
            if each[1] == 0:
                key[each[0]] = True
                each[0] = None
                each[1] = None

    notEnd = False
    for each in order:
        if key[each] == False:
            toContinue = True
            for worker in workers:
                if each == worker[0]:
                    toContinue = False
            if not toContinue:
                continue

            notEnd = True
            if steps[each] is None:
                for worker in workers:
                    if worker[0] is None:
                        worker[0] = each
                        worker[1] = ord(each) - 64 + 60
                        break
            else:
                allGood = True
                for letter in steps[each]:
                    if key[letter] is False:
                        allGood = False
                if allGood:
                    for worker in workers:
                        if worker[0] is None:
                            worker[0] = each
                            worker[1] = ord(each) - 64 + 60
                            break
    for each in workers:
        if each[1] is not None:
            notEnd = True

    if notEnd:
        x += 1
print(x) #Merry Christmas :)
