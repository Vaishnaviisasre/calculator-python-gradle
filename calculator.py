import sys

def calculate(num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2
    else:
        return "Invalid operation!"

# Ensure correct number of arguments (3 arguments expected: num1, num2, operation)
if len(sys.argv) != 4:
    print("Usage: python calculator.py <num1> <num2> <operation>")
    sys.exit(1)

# Perform the calculation
result = calculate(sys.argv[1], sys.argv[2], sys.argv[3])
print("Result:", result)
<<<<<<< HEAD
=======

>>>>>>> 86c8898 (Add Gradle wrapper)
