#ranges = [
#    [['x1','y1'],['x2','y2']]
#    []
#    []
#   ]
f = open('input').read().splitlines()

def gRanges(l):
    r0 = [_.split('->') for _ in l]
    r1 = [e.replace(' ','') for i in r0 for e in i]
    r2 = [_.split(',') for _ in r1]
    r3 = [r2[_:_+2] for _ in range(0, len(r2), 2)]
    return r3

def cMatrix(xy):
    x = 0
    y = 0
    for i in xy:
        for e in i:
            if int(e[0]) > x:
                x = int(e[0])
            if int(e[1]) > y:
                y = int(e[1])
    m = [['.' for _ in range(x)] for _ in range(y)]
    return m

def gInterlude(jose):
    x1 = int(jose[0][0])
    y1 = int(jose[0][1])
    x2 = int(jose[1][0])
    y2 = int(jose[1][1])
    interlude = [jose[0], jose[1]]

    if x1 < x2:
        for x in range(x1, x2+1):
            print(x)
        print()
    if x1 > x2:
        for x in range(x1, x2-1, -1):
            print(x)
        print()
    if x1 == x2:
        print(x1)

    if y1 < y2:
        for x in range(y1, y2+1):
            print(x)
        print()
    if y1 > y2:
        for x in range(y1, y2-1, -1):
            print(x)
        print()
    if y1 == y2:
        print(x1)
    # List comprehension x and y
    # max or min
    # zip

r = gRanges(f)
m = cMatrix(r)

c = 0
for i in range(3):
    gInterlude(r[i])