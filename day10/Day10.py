import matplotlib.pyplot as plt
with open('file.in') as f:
    content = f.readlines()
content = [x.strip() for x in content]
coordinates = [[] for x in content]
for i, row in enumerate(content):
    coordinates[i].append(int(row[row.find('<') + 1:row.find(',')]))
    coordinates[i].append(int(row[row.find(',') + 1: row.find('>')]))
    new_row = row[row.find('>') + 1:]
    coordinates[i].append(int(new_row[new_row.find('<') + 1:new_row.find(',')]))
    coordinates[i].append(int(new_row[new_row.find(',') + 1: new_row.find('>')]))
count = 0
first = True
lastx = 0
lasty = 0
finalx = []
finaly = []
newplot = False
while True:
    count += 1
    x = []
    y = []
    for each in coordinates:
        each[0] += each[2]
        x.append(each[0])
        each[1] += each[3]
        y.append(each[1])
    currentx = len(set(x))
    currenty = len(set(y))

    if first:
        first = False
        lastx = currentx
        lasty = currenty
    else:

        if lastx > currentx:
            lastx = currentx
            finalx = list(x)
            newplot = True
        if lasty > currenty:
            lasty = currenty
            finaly = list(y)
            newplot = True

        if newplot and finalx and finaly:
            print(count) #As it happens, I didn't have time to create a machine learning algorithm to recognize letter, so each time there were less and less different
            #points, I had it draw a graph. I had to install plotly to make plotting the points easier. It is about the 5th or 6th image. You could have it stop when the numbers
            #go back up again, but I just ctrl C'd it.
            for i, x in enumerate(finalx):
                plt.scatter(x, finaly[i])
            plt.show()
            plt.clf()
    del x
    del y


