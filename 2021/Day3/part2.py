f = open('input', mode="rt", encoding="utf-8")
o2 = []
co2 = []
for l in f:
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
x, y = getBits(o2, 3)
print(x, y)

#TODO: if len list = 2 ...
#TODO: def bitsCounter
#TODO: def clearList