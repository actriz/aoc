with open("input") as i:
    gamma = ""
    epsilon = ""
    f = i.read().split()
    fullLen = len(f)
    elementLen = len(f[0])
    for i in range(elementLen):
        c0 = 0
        c1 = 0
        for j in range(fullLen):
            x = int(f[j][i])
            if x == 0:
                c0 += 1
            elif x == 1:
                c1 += 1
        if c0 > c1:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
print(int(gamma, 2) * int(epsilon, 2))
