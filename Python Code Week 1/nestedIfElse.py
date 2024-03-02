#============== POSITIVE OR NEGATIVE =====================

# # Getting user's input
# num = int(input("Enter a random whole number: "))


# # Check if the number is positive, negative, or zero
# if num > 0:
#     print("The number you entered is positive.")
# elif num < 0:
#     print("The number entered is negative.")
# else:
#     print("The number given is zero.")


    #==================================================================#

# DOING SAME AS ABOVE BUT WITH FUNCTIONS

def posORneg():
    num = int(input("Enter a whole number: "))

    if num > 0:
        print(f"{num} has a positive value")
    elif num < 0:
        print(f"{num} has a negative value")
    else:
        print(f"{num} has a value of zero")

posORneg()

