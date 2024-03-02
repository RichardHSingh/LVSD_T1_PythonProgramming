#============== COMPARING NUMBERS =====================

# # getting first user input
# num1 = int(input("Please enter the first number: "))

# # getting second user input
# num2 = int(input("Please enter the second number: "))


# # using if else statement to see which is true
# if num1 > num2:
#     print("{} is greater than {}" .format(num1,num2))
# elif num1 == num2:
#     print("Both digits are of equal value")
# else:
#     print("{} is small than {}" .format(num1,num2))


#==================================================================#
    
#============== COMPARING NUMBERS FUNCTION =====================

# turning above into a function

# getting input from user
def comparison():
    num1 = int(input("Please enter a whole number: "))
    num2 = int(input("Please enter a second whole number"))

# using if else statement to see which is true
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1 == num2:
        print(f"both numbers are of equal value")
    else:
        print(f"{num1} is smaller than {num2}")

# calling the function and printing appropriate outcome based on input
comparison()



