f = open("input").read().split()
ROCK = 1
PAPER = 2
SCISSORS = 3
LOST = 0
DRAW = 3
WIN = 6
p1 = 0
p2 = 0


def game(input):
    l = []
    s = 2
    for i in range(0, len(f), s):
        l.append(f[i : i + s])
    return l


def part1(uA, uB):
    global p1
    if uB == "X":
        if uA == "C":
            p1 += ROCK + WIN
        elif uA == "A":
            p1 += ROCK + DRAW
        else:
            p1 += ROCK
    if uB == "Y":
        if uA == "A":
            p1 += PAPER + WIN
        elif uA == "B":
            p1 += PAPER + DRAW
        else:
            p1 += PAPER
    if uB == "Z":
        if uA == "B":
            p1 += SCISSORS + WIN
        elif uA == "C":
            p1 += SCISSORS + DRAW
        else:
            p1 += SCISSORS


def part2(uA, uB):
    global p2
    if uB == "X":  # LOSE
        if uA == "C":
            p2 += PAPER
        elif uA == "A":
            p2 += SCISSORS
        else:
            p2 += ROCK
    if uB == "Y":  # DRAW
        if uA == "A":
            p2 += ROCK + DRAW
        elif uA == "B":
            p2 += PAPER + DRAW
        else:
            p2 += SCISSORS + DRAW
    if uB == "Z":  # WIN
        if uA == "B":
            p2 += SCISSORS + WIN
        elif uA == "C":
            p2 += ROCK + WIN
        else:
            p2 += PAPER + WIN


for i in game(f):
    part1(i[0], i[1])
    part2(i[0], i[1])
print(p1)
print(p2)
