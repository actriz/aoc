s, m = open('input').read().split('\n\n')
one = [[] for i in range(9)]
two = [[] for i in range(9)]

for l in s.split('\n')[:-1]:
    p = 0
    for w in range(1, len(l), 4):
        if l[w] != ' ':
            one[p] += l[w]
            two[p] += l[w]
        p += 1

for n in m.split('\n'):
    a, f, t = int(n.split()[1]), int(n.split()[3])-1, int(n.split()[5])-1
    for x in range(a):
        one[t].insert(0, one[f][0])
        one[f].pop(0)
    for x in reversed(range(a)):
        two[t].insert(0, two[f][x])
        two[f].pop(x)

for p1, p2 in zip(one, two):
    #print(p1[0], end="")
    print(p2[0], end="")