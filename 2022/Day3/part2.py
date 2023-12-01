import string

f = open("input").read().split()
a = list(string.ascii_lowercase)
aLower = [i for i in range(1, 26 + 1)]
aUpper = [i for i in range(27, 52 + 1)]
n_index = []


def group3(v):
    arr = []
    s = 3
    for index in range(0, len(v), s):
        arr.append(v[index : index + s])
    return arr


def eq(a):
    return list(set(a[0]) & set(a[1]) & set(a[2]))


def num(l, a):
    global n_index
    for i in range(len(a)):
        if l == a[i].upper():
            n_index.append(aUpper[i])

        if l == a[i].lower():
            n_index.append(aLower[i])


arr = group3(f)
for i in range(len(arr)):
    l = eq(arr[i])
    num(l[0], a)
print(sum(n_index))
