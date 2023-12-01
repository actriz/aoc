with open("input") as i:
    h = 0
    d = 0
    for l in i:
        x = l.split()
        x2 = int(x[1])
        if x[0] == "forward":
            h = h + x2
        elif x[0] == "down":
            d = d + x2
        elif x[0] == "up":
            d = d - x2
print(h * d)
