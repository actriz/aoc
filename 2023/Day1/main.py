f = open("input").read().split("\n")


def rmchars(d):
    numbers = []
    for e in range(len(d)):
        t = ""
        for c in range(len(d[e])):
            if d[e][c].isnumeric():
                t += d[e][c]
        numbers.append(t)
    return numbers


def digit(d):
    new = []
    for x in d:
        if len(str(x)) == 1:
            new.append(x + x)
        else:
            new.append(x[0] + x[-1])
    return [int(_) for _ in new]


def tree(d):
    new = []
    for e in range(len(d)):
        t = ""
        for phrase in range(len(d[e])):
            if d[e][phrase:][0].isdigit():
                t += d[e][phrase][0]
                continue
            if d[e][phrase:].startswith("one"):
                t += "1"
                continue
            if d[e][phrase:].startswith("two"):
                t += "2"
                continue
            if d[e][phrase:].startswith("three"):
                t += "3"
                continue
            if d[e][phrase:].startswith("four"):
                t += "4"
                continue
            if d[e][phrase:].startswith("five"):
                t += "5"
                continue
            if d[e][phrase:].startswith("six"):
                t += "6"
                continue
            if d[e][phrase:].startswith("seven"):
                t += "7"
                continue
            if d[e][phrase:].startswith("eight"):
                t += "8"
                continue
            if d[e][phrase:].startswith("nine"):
                t += "9"
                continue
        new.append(t)
    return new


p1 = rmchars(f)
p1_2 = digit(p1)
print(sum(p1_2))


p2 = tree(f)
p2_2 = digit(p2)
print(sum(p2_2))
