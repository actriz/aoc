with open('input') as i:
    ns = [int(l) for l in i]
acNums = (ns[0]+ns[1]+ns[3])
increased = 0
for x in range(len(ns)-2):
    acumNew = (ns[x] + ns[x+1] + ns[x+2])
    if acumNew > acNums:
        increased += 1
    acNums = acumNew
print(increased)