n = int(input("Enter the Number for checking the factors:"))
num = n
result =[]

for i in range(1,num//2):
    if num%i==0:
        result.append(i)
result.append(num)
print(result)  #better solution