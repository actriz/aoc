with open('input') as i:
    h = 0
    d = 0
    a = 0
    for l in i:
        x=l.split()
        x1=int(x[1])
        if x[0] == 'down':
            a = a + x1
        elif x[0] == 'up':
            a = a - x1
        elif x[0] == 'forward':
            h = h + x1
            d = d + (a*x1)
print(h*d)