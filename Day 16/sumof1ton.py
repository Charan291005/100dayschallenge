def func(sum,i,n):
    if i > n:
        print(sum)
        return 0
    func(sum+i,i+1,n)

func(5,4,4)