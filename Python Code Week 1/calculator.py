 #============== SIMPLE CALCULATOR =====================

print("Welcome to the THE GAME..!\n")

# User inputs the first number
num1 = float(input("Enter the first number: "))

# Operator type 
operator = input("Enter an operator (+ , - , * or  /): ")

# User enters second digit
num2 = float(input("Enter the second number: "))

# Perform calculations based on the operator entered
if operator == "+":
    result = num1 + num2
    print(f"The sum of {num1} + {num2} is: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The sum of {num1} - {num2} is: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"The sum of {num1} * {num2} is: {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The sum of {num1} / {num2} is: {result}")
    else:
        print("ERROR!: Cannot divide by zero")
else:
    print("Invalid operator. Please enter +, -, *, or /.")

# console closes
input("To continue.. Press Enter or Escape to exit")
