import numpy as np

f = open('input').read().split()

def createLists(listado):
    n = 25
    numbers = listado[0].split(',')
    cartons = [listado[i:i+n] for i in range(1, len(listado), n)]
    return numbers, cartons

def correctCartons(listado):
    finalCartons = []
    n = 5
    for x in range(len(listado)):
        tempList = listado[x]
        output = [tempList[i:i+n] for i in range(0, len(tempList), n)]
        finalCartons.append(output)
    return finalCartons

def markBingo(integer, game):
    for c in range(len(game)):
        for f in range(len(game[c])):
            for n in range(len(game[c][f])):
                if game[c][f][n] == integer:
                    game[c][f][n] = 'X'
    return game

def checkWin(joses, n):
    for c in joses:
        for f in c:
            if all(i == 'X' for i in f):
                return c, n
    for c in joses:
        a = [f for f in c]
        x = np.transpose(a)
        for i in x:
            if all(n == 'X' for n in i):
                return c, n

def winner(sufle, mawik):
    s = 0
    for x in sufle:
        for n in x:
            if n != 'X':
                s += int(n)
    print(s*int(mawik))

numbers, c = createLists(f)
cartons = correctCartons(c)

for i in range(len(numbers)):
    markBingo(numbers[i], cartons)
    if checkWin(cartons, numbers[i]) is not None:
        uno, dos = checkWin(cartons, numbers[i])
        break

winner(uno, dos)