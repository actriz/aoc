f = open('input').read().split('\n')
c0 = []
a = 0
for i in range(len(f)):
    if len(f[i])>0:
        a += int(f[i])
    if i == len(f)-1:
        c0.append(a)
        a = 0
    if f[i] == '':
        c0.append(a)
        a = 0
p1 = max(c0)
c1 = sorted(c0)
p2 = c1[-1]+c1[-2]+c1[-3]
print(p1)
print(p2)