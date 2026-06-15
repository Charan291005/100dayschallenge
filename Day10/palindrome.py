from typing import Any

n = int(input("Enter a number: "))
num = n
result = 0
while num > 0:
    ld = num % 10
    result = (result * 10) + ld
    num = num // 10

if result == n:
    print("The number is palindrome")

else:
    print("The number is not palindrome")
