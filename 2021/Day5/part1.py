#ranges = [
#    [['x1','x2'],['y1','y2']]
#    []
#    []
#   ]
f = open('input').read().splitlines()

def getRanges(l):
    r0 = [_.split('->') for _ in l]
    r1 = [e.replace(' ','') for i in r0 for e in i]
    r2 = [_.split(',') for _ in r1]
    r3 = [r2[_:_+2] for _ in range(0, len(r2), 2)]
    return r3

r = getRanges(f)
print(r)