f = open('input').read().splitlines()

path = '/root'
dirs = ['/root']
size = [0]

for l in f:
    if l[0] == '$':
        if l[2:4] == 'ls': pass
        if l[2:4] == 'cd':
            if l[5:6] == '/': path = '/root'
            elif l[5:7] == '..': path = path[:path.rfind('/')]
            else:
                path = path + '/' + l[5:]
                if path not in dirs:
                    dirs.append(path)
                    size.append(0)
    elif l[0:3] == 'dir':
        pass
    else:
        n = int(l[:l.find(' ')])
        d = path
        size[dirs.index(d)] += n
        for _ in range(d.count('/')-1):
            d = d[:d.rfind('/')]
            size[dirs.index(d)] += n

x = 30000000 - (70000000 - size[dirs.index('/root')])

p1 = [s for s in size if s <= 100000]
p2 = [s for s in size if s >= x]

print(sum(p1))
print(min(p2))