"""
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""
f = open('input').read().splitlines()

def ranges(l):
    r0 = [_.split('->') for _ in l]
    r1 = [e.replace(' ','') for i in r0 for e in i]
    r2 = [_.split(',') for _ in r1]
    r3 = [r2[_:_+2] for _ in range(0, len(r2), 2)]
    return r3

def matrix(xy):
    x = 0
    y = 0
    for i in xy:
        for e in i:
            if int(e[0]) > x:
                x = int(e[0])
            if int(e[1]) > y:
                y = int(e[1])
    m = [[0 for _ in range(x)] for _ in range(y)]
    return m

def interlude(jose):
    interlude = []
    [[x1,y1],[x2,y2]] = jose

    if int(y1)==int(y2):
        if int(x1)<int(x2):
            for i in range(int(x1),int(x2)+1):
                interlude.append([i, y1])
        else:
            for i in range(int(x2),int(x1)+1):
                interlude.append([i, y1])

    if int(x1)==int(x2):
        if int(y1)<int(y2):
            for i in range(int(y1),int(y2)+1):
                interlude.append([i, x1])
        else:
            for i in range(int(y2),int(y1)+1):
                interlude.append([i, x1])

r = ranges(f)
m = matrix(r)

for i in range(len(r)):
   interlude(r[i])