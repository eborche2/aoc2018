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
    if step not in steps:
        steps[step] = []
    steps[step].append(pre)
steps = collections.OrderedDict(sorted(key.items()))
key = collections.OrderedDict(sorted(key.items()))
notFound = True
for letter, found in steps.items():
    found.sort()
def findFirstLetter(letters):
    return letters
while notFound:
    current = None
    for letter, found in key.items():
        if not found:
            if not steps[letter]:
                key[letter] = True
                break
            else:
                findFirstLetter(steps[letter])


print(key, steps)
