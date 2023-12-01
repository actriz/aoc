with open("input") as i:
    ns = [int(l) for l in i]
    inc = 0
    n = ns[0]
    for x in ns:
        if x > n:
            inc += 1
        n = x
    print(inc)
