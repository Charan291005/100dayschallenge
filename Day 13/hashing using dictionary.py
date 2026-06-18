n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]


counts = {}


for num in n:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1


for num in m:
    if num in counts:
        print(counts[num])
    else:
        print(0)