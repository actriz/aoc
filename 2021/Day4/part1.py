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

def checknumber(integer, game):
    for c in range(len(game)):
        for f in range(len(game[c])):
            for n in range(len(game[c][f])):
                if game[c][f][n] == integer:
                    game[c][f][n] = 'X'
    return game

def checkWin():
    pass

numbers, c = createLists(f)
cartons = correctCartons(c)
changed = checknumber(numbers[0], cartons)
print(changed)