f = open('input')
text = f.read().split()
o2 = []
co2 = []
for l in text:
    o2.append((l))
    co2.append((l))
f.close()
print(o2)

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

def clearList(list, bit, position):
    return [x for x in list if int(x[position]) == bit]

x, y = getBits(o2, 0)
m = clearList(o2, x, y)

# if len list = 2 ...
# def clearList