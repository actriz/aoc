with open('input') as i:
    ns = []
    for l in i:
        x = int(l)
        ns.append(x)
    inc = 0
    n = ns[0]
    for x in ns:
        if x > n:
            inc += 1
        n = x
    print(inc)