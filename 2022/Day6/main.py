f = open("input").read()


def marker(t, n):
    for i in range(len(t) - n):
        if len(set(t[i : i + n])) == n:
            print(i + n)
            break


marker(f, 4)
marker(f, 14)
