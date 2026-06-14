def calculator():
    while True:
        print("\n--- Simple Calculator ---")
        print("Operations: +, -, *, /")
        print("Type 'quit' to exit\n")
        
        user_input = input("Enter first number: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        try:
            num1 = float(user_input)
        except ValueError:
            print("Invalid number. Try again.")
            continue
        
        operator = input("Enter operator (+, -, *, /): ")
        if operator not in ['+', '-', '*', '/']:
            print("Invalid operator. Try again.")
            continue
        
        try:
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Try again.")
            continue
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero!")
                continue
            result = num1 / num2
        
        print(f"Result: {num1} {operator} {num2} = {result}")

calculator()
