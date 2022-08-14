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

def xyz(x1,y1,x2,y2):
    xs = []
    ys = []
    l = 0
    if x1==x2:
        xs.append(x1)
    if y1==y2:
        ys.append(y1)
    if x1<x2:
        for i in range(x1, x2+1):
            xs.append(i)
    if y1<y2:
        for i in range(y1, y2+1):
            ys.append(i)
    if x1>x2:
        for i in range(x1, x2-1,-1):
            xs.append(i)
    if y1>y2:
        for i in range(y1, y2-1,-1):
            ys.append(i)
    if len(xs)>len(ys):
        l = len(xs)
    else:
        l = len(ys)
    return xs, ys, l

def interlude(jose):
    interlude = []
    x1 = int(jose[0][0])
    y1 = int(jose[0][1])
    x2 = int(jose[1][0])
    y2 = int(jose[1][1])
    xlist, ylist, l = xyz(x1,y1,x2,y2)
    
    for i in range(l):
        x=0
        y=0
        try:
            x=xlist[i]
            y=ylist[i]
        except IndexError:
            if len(xlist)==1:
                x=xlist[0]
            else:
                x=xlist[i]
            if len(ylist)==1:
                y=ylist[0]
            else:
                y=ylist[i]
        
        interlude.append((x,y))
    return interlude

def mark(mawik, aron):
    for n in aron:
        x, y = n
        mawik[y-1][x-1] += 1

r = ranges(f)
m = matrix(r)

for i in range(len(r)):
   i = interlude(r[i])
   mark(m, i)