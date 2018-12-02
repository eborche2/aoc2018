
with open('file.in') as f:
    content = f.readlines()
content = [x.strip() for x in content]
twocount = 0
threecount = 0
for each in content:
    thisSet = set(each[:])
    done2 = False
    done3 = False
    for letter in thisSet:
        if each.count(letter) == 2 and not done2:
            twocount += 1
            done2 = True
        if each.count(letter) == 3 and not done3:
            threecount += 1
            done3 = True
        if done2 and done3:
            break
print(twocount * threecount) # Solution 1
original = len(content)
for i in range(original):
    if i == original -1:
        break
    else:
        n = i + 1
    for z in range(n,original):
        count = 0
        badletter = 0
        for l, letter in enumerate(content[i]):
            if letter != content[z][l]:
                count +=1
                badletter = l
            if count > 1:
                break
        if count == 1:
            content[i] = content[i][:badletter] + content[i][badletter+1:]
            print(content[i]) # Solution 2
