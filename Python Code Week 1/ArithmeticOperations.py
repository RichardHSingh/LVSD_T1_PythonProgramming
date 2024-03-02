#============== MATHMETICS =====================

# Arithmetic Operations: Write a program that takes two numbers as input and performs addition, subtraction, multiplication, and division.

print("Welcome to THE BASICS..")

# prompt user to enter first number
num1 =  int(input("Please enter a whole number to begin calculation.."))

# prompt user to enter an operator
operator = input("Enter an operator (+ , - , * or  /): ")

# prompt user to enter second number
num2 = int(input("Please enter a second number to sum up with first digit"))

# creating statement to calclate the digits and operator used
calculate = ("Sum of your input digits {} {}  {} = ".format(num1,operator,num2))

print(calculate)
print = (f"Sum of your input digits {num1} {operator}  {num2} = ")


#==================================================================#


#============== MATHMETICS FUNCTION =====================

# turning the code above into a function 
def arithmetic(num1,operator,num2):
    print("Time to MATHS")
    
    # checking what kind of operator the user has imputed and and appropraitely utilising the operator
    if operator == '+':
        calculate = num1 + num2
    elif operator == '-':
        calculate = num1 - num2
    elif operator == '*':
        calculate = num1 * num2
    elif operator == '/':
        if calculate != 0:
            calculate = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return None
    else:
        print("Error: Invalid operator used.")
        return None

    return calculate

# getting digits and operator from user using input
# int for input makes sure the inut is a number
num1 = int(input("Please enter a whole number to begin calculation.. "))
operator = input("Enter an operator (+ , - , * or  /): ")
num2 = int(input("Please enter a second number to calculate with first.. "))

# statement for getting all the input then if the input is not empty = print appropraite answer
calculate = arithmetic(num1, operator, num2)

if calculate is not None:
    print(f"Result of the operation {num1} {operator} {num2} = {calculate}")




