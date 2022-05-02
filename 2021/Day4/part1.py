f = open('./input').read().split()

def createLists(listado):
    n = 25
    numbers = listado[0].split(',')
    cartons = [ listado[i:i + n] for i in range(1, len(listado),25)]
    return numbers, cartons

def correctCartons(listado):
    finalCartons = []
    n = 5
    for x in range(len(listado)):
        tempList = listado[x]
        output = [tempList[i:i + n] for i in range(0, len(tempList), n)]
        finalCartons.append(output)
    return finalCartons

def checknumber():
    pass
    
def checkWin():
    pass

n, c0 = createLists(f)
c = correctCartons(c0)
    