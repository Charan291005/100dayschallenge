def missing_number(arr,n):

    total = n*(n+1)//2
    actual = sum(arr)

    missing = total - sum(arr)

    return missing

arr = [1,2,4,5]
n = 5
print(missing_number(arr,n))