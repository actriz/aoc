f = open("input")
text = f.read().split()
o2 = co2 = text
f.close()


def getBitso2(listado, position):
    c0 = 0
    c1 = 0
    for i in listado:
        if i[position] == "0":
            c0 += 1
        else:
            c1 += 1
    if c0 > c1:
        return 0, position
    elif c0 == c1:
        return 1, position
    else:
        return 1, position


def getBitsco2(listado, position):
    c0 = 0
    c1 = 0
    for i in listado:
        if i[position] == "0":
            c0 += 1
        else:
            c1 += 1
    if c0 > c1:
        return 1, position
    elif c0 == c1:
        return 0, position
    else:
        return 0, position


def clearList(listado, bit, position):
    return [x for x in listado if int(x[position]) == bit]


for x in range(len(o2[0])):
    if len(o2) == 1:
        break
    else:
        b, p = getBitso2(o2, x)
        o2 = clearList(o2, b, p)

for x in range(len(co2[0])):
    if len(co2) == 1:
        break
    else:
        b, p = getBitsco2(co2, x)
        co2 = clearList(co2, b, p)

n_o2 = int(o2[0], 2)
n_co2 = int(co2[0], 2)
print(n_o2 * n_co2)
