#============== WELCOMING USER =====================

# welcoming user to THE GAME
# getting users input of name ans saving it in variable with will welcome them later with given name
name = input("What name shall I address thee with...?")

print("Welcome to THE GAME, " + name)


#==================================================================#

# as above but with use of function
#creating function for greeting user
def welcomePlayer():
    name = input("What name shall I address thee with...?")
    print("Welcome to THE GAME, " + name)

# Call the function to execute the code
welcomePlayer()