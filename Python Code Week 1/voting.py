#============== VOTING ELEGIBILITY =====================

# # Find out now if you are eligible to cast a vote

# print("Want to vote?? Find out if you're eligible...")
# print("=============================================\n")

# # taking user age
# userAge = int(input("Please enter your age : "))

# # if the age input is less than 18 years
# if userAge < 18:    
#     print(f"Sorry, You are currently {userAge} and not eligible to cast a vote.\n")
#     print(f"You will be able to vote {18-userAge} year(s) from now.")
# else:
#     print("Congratulations! You are definitley able to vote during the next election.")


    #==================================================================#

# checkign is user can vote but using of function
def voting():
    print("Want to vote?? Find out if you're eligible...")

    userAge = int(input("Please enter your age : "))

    # if the age input is less than 18 years
    if userAge < 18:    
        print(f"Sorry, You are currently {userAge} and not eligible to cast a vote. You can vote in {18-userAge} year(s) times.\n")
    else:
        print("Congratulations! You are definitley able to vote during the next election.")

# calling function to print appropriate outcome
voting()

