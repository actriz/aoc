with open('input') as i:
    gamma = ""
    epsilon = ""
    file = i.read().split()
    TotalLen = len(file)
    ElementLen = len(file[0])
    for i in range(ElementLen):
        c0 = 0
        c1 = 0
        for j in range(TotalLen):
            x=int(file[j][i])
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
answer = int(gamma, 2) * int(epsilon, 2)
print(answer)