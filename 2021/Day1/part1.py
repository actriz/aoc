with open('input') as i:
    nums = []
    for line in i:
        x = int(line)
        nums.append(x)
    acumIncreased = 0
    n = nums[0]
    for x in nums:
        if x > n:
            acumIncreased += 1
        n = x
    print(acumIncreased)