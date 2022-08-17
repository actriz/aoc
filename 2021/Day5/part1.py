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
    m = [[0 for _ in range(x+1)] for _ in range(y+1)]
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
        mawik[y][x] += 1

def check(table):
    c = 0
    for h in table:
        for n in h:
            if n >= 2:
                c += 1
    print(c)

r = ranges(f)
m = matrix(r)

for i in range(len(r)):
    [[x1, x2], [y1, y2]] = r[i]
    if x1 == y1 or x2 == y2:
        i = interlude(r[i])
        mark(m, i)
check(m)