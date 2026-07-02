num = [3,5,7,2,9,6]


def func(num,left,right):
    if left>=right:
        return

    num[left],num[right] = num[right],num[left]
    func(num,left+1,right-1)

func(num,3,4)
print(num)