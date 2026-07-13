num = [5,7,8,1,2,6]
def selection_Sort(num):
    n = len(num)
    for i in range(0,n):
        mini_ind = i
        for j in range(i+1,n):
            if num[j] < num[mini_ind]:
                mini_ind = j

        num[i],num[mini_ind] = num[mini_ind], num[i]

selection_Sort(num)
print(num)