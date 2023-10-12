import math
print("Available operations:\n 1. Addition (+)\n 2. Subtraction (-)\n 3. Multiplication (*)\n 4. Division (/)\n 5. Extract root (root)\n 6. Raise to degree (degree)")
choice = input("Select operation (enter the appropriate number): ")

if choice in ('1', '2', '3', '4', '5', '6'):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = num1 + num2
        operation = "+"
    elif choice == '2':
        result = num1 - num2
        operation = "-"
    elif choice == '3':
        result = num1 * num2
        operation = "*"
    elif choice == '4':
        result = num1 / num2
        operation = "/"
    elif choice == '5':
        result = math.sqrt(num1)
        operation = "root"
    elif choice == '6':
        result = num1 ** num2
        operation = "degree"

    print(f"Result: {num1} {operation} {num2} = {result}")
else:
    print("Wrong choice of operation.")
