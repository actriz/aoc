f = open('input')
text = f.read().split()
o2 = []
co2 = []
for l in text:
    o2.append((l))
    co2.append((l))
f.close()

def getBits(list, position):
    c0 = 0
    c1 = 0
    for i in list:
        if i[position] == "0":
            c0 += 1
        else:
            c1 += 1
    if c0 > c1:
        return 0, position
    else:
        return 1, position

def clearList(list, position, bit):
    return [x for x in list if int(x[position]) == bit]

x, y = getBits(o2, 0)
clearList(o2, y, x)

# if len list = 2 ...
# for i in range(2)
    # for x in range(len(list[x]))
        # if len list = 2 ...
        # def
        # def