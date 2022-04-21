with open('input') as i:
    nums = []
    for line in i:
        x = int(line)
        nums.append(x)

acumNum = (nums[0]+nums[1]+nums[3])
acumIncreased = 0
for x in range(len(nums)-2):
    acumNew = (nums[x] + nums[x+1] + nums[x+2])
    if acumNew > acumNum:
        acumIncreased += 1
    acumNum = acumNew
print(acumIncreased)