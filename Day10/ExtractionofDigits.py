
n = int(input("Enter your number:"))
num = n


while n > 0:
    lastdigit = n%10
    print(lastdigit)
    n = n//10
