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
    # List comprehension x and y
    # max/min
    # zip
    # diff ranges

r = gRanges(f)
m = cMatrix(r)

for i in range(1):
    gInterlude(r[i])