f = open("input").read().split("\n")
acc = 0
for phrase in range(len(f)):
    block = f[phrase].split(":")
    sets = block[1].split(";")
    neg = True
    for cube in range(len(sets)):
        colornumber = sets[cube].split(",")
        for colnum in colornumber:
            data = colnum.split(" ")
            if (
                (data[2] == "red" and int(data[1]) > 12)
                or (data[2] == "blue" and int(data[1]) > 14)
                or (data[2] == "green" and int(data[1]) > 13)
            ):
                neg = False
            else:
                continue
    if neg == True:
        acc += phrase + 1
print(acc)
