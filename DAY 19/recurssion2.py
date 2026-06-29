def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)

# Taking input from the user
num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))