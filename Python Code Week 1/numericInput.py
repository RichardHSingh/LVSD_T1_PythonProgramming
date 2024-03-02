#============== CALCULATING INPUT FROM USER =====================

print("Welcome to the MATHEMATICS..! We will be summing up the input of your two digits\n")

# User inputs the first number
num1 = int(input("Please enter the first number: "))

# User enters second digit
num2 = int(input("Please enter the second number: "))

# Calculates the sum of the entered numbers
sum_result = num1 + num2

# printing string with given inuput numbers and the results
print("Sum of your entered digits ", num1, " and" , num2, " is", sum_result)


#==================================================================#

# AS ABOVE BUT WITH FUNCTION
# creating function for numeric function to get sum of 2 digits entered
def numericInput():
    print("Welcome to the MATHEMATICS..! We will be summing up the input of your two digits")
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("PLease enter the second number: "))
    sum_result = num1 + num2
    print(f"Sum of your entered digitrs {num1} and {num2} is {sum_result}")

#calling the function above
numericInput()