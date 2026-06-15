n = int(input("Enter a number: "))
num = n
total = 0
nod = len(str(n))

while num>0:
    ld = num%10
    total = total + (ld**nod)
    num=num//10

if total == n:
    print("YES")

else:
    print("NO")
