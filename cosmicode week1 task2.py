# Task 2: Advanced Arithmetic Operations with User Input and Choice
def power(base, exponent):
    return base ** exponent

def modulo(dividend, divisor):
    return dividend % divisor

# Get user input for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask user which operation to perform
print("\nSelect an operation:")
print("1. Power (first number raised to second number)")
print("2. Modulo (first number modulo second number)")
choice = input("Enter your choice (1 or 2): ")

# Perform the selected operation and display result
if choice == '1':
    result = power(num1, num2)
    print(f"\nResult: {num1} ^ {num2} = {result}")
elif choice == '2':
    result = modulo(num1, num2)
    print(f"\nResult: {num1} % {num2} = {result}")
else:
    print("Invalid choice! Please select 1 or 2.")