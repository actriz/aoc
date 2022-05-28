with open('input') as i:
    ns = []
    for l in i:
        x = int(l)
        ns.append(x)
acNums = (ns[0]+ns[1]+ns[3])
Increased = 0
for x in range(len(ns)-2):
    acumNew = (ns[x] + ns[x+1] + ns[x+2])
    if acumNew > acNums:
        Increased += 1
    acNums = acumNew
print(Increased)