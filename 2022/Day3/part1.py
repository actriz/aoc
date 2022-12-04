import string
f = open('input').read().split()
a = list(string.ascii_lowercase)
aLower = [i for i in range(1,26+1)]
aUpper = [i for i in range(27,52+1)]
n_index = []

def divi(v):
    n = len(v)//2
    return [v[0:n], v[n:]]

def eq(l1, l2):
    return list(set(l1) & set(l2))

def num(l, a):
    global n_index
    for i in range(len(a)):
        if l == a[i].upper():
            n_index.append(aUpper[i])
        if l == a[i].lower():
            n_index.append(aLower[i])

for e in f:
    arr = divi(e)
    l = eq(arr[0], arr[1])
    num(l[0], a)
print(sum(n_index))