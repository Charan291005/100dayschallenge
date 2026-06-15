n = int(input("Enter your Number to count"))

count = 0
while n > 0:
  count += 1
  n = n//10

print(count)