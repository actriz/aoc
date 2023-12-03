f = open("input").read().split("\n")
acc = 0
for phrase in range(len(f)):
    block = f[phrase].split(":")
    sets = block[1].split(";")
    red = 0
    blue = 0
    green = 0
    for cube in range(len(sets)):
        colornumber = sets[cube].split(",")
        for colnum in colornumber:
            data = colnum.split(" ")
            if (data[2] == "red") and (int(data[1]) > red):
                red = int(data[1])
            if (data[2] == "blue") and (int(data[1]) > blue):
                blue = int(data[1])
            if (data[2] == "green") and (int(data[1]) > green):
                green = int(data[1])
    acc += red * blue * green
print(acc)
