f = open('input').read().split()
p1 = 0
p2 = 0

def pair(arr):
    return [vector.split('-') for vector in arr.split(',')]

def alert(vector):
    global p1, p2
    [[x1, x2], [y1, y2]] = vector
    one = [i for i in range(int(x1), int(x2)+1)]
    two = [i for i in range(int(y1), int(y2)+1)]
    if (int(x1) <= int(y1) and int(x2) >= int(y2)) or (int(y1) <= int(x1) and int(y2) >= int(x2)):
        p1 += 1
    if (any([i in two for i in one])) or (any([i in one for i in two])):
        p2 += 1

for p in f:
    alert(pair(p))
print(p1, p2)