nums = [5,7,8,5,6,1,3,2]
f_map = dict()
for i in range(0,len(nums)):
    if nums[i] in f_map:
        f_map[nums[i]] += 1
    else:
        f_map[nums[i]] = 1
print(f_map)