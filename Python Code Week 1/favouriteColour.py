#============== USER'S FAV COLOUR =====================

# Asking the user to enter their favourite colour
favouriteColor = input("Please enter your favourite colour: ")

# Display a message with given answer
print("Oh WOAH! " + favouriteColor + " is a ok but RED IS BETTER!.")


#==================================================================#

# ================== TURNING ABOVE CODE INTO FUNCTION =================
def favouriteColour():
    favouriteColour = input("Please enter your favourite colour: ")
    print(f"OH WOAH! {favouriteColour} is nice BUT red is so much cooler")

#calling the colour function
favouriteColor()

