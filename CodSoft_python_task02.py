print("Welcome to Enhanced Calculator!")
print("Operations available: +, -, *, /, ^, %\n")

while True:
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operation (+, -, *, /, ^, %): ").strip()
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.\n")
        continue

    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '^': lambda a, b: a ** b,
        '%': lambda a, b: a % b
    }

    if operator not in operations:
        print("Invalid operator. Please use +, -, *, /, ^, %\n")
        continue

    if operator in ['/', '%'] and num2 == 0:
        error = "Division by zero" if operator == '/' else "Modulus by zero"
        print(f"Error: {error} is not allowed.\n")
        continue

    result = operations[operator](num1, num2)
    print(f"\nResult: {num1} {operator} {num2} = {result}")

    another = input("\nPerform another calculation? (yes/no): ").lower()
    if another not in {'yes', 'y'}:
        print("\nGoodbye!")
        break

    print("\n" + "=" * 30 + "\n")