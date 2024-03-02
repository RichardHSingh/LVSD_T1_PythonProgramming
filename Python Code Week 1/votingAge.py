# Checking if one is old enough to vote or not
# Find out now if you are eligible to cast a vote

print("Find out if you're eligible to vote...")
print("========================================\n")

votingAge = int(input("Please enter your age : "))

# if the age input is less than 18 years
if votingAge < 18:    
    print("Sorry, You are currently {} and not eligible to cast a vote.\n\n".format(votingAge))
    print("You will be able to vote {} year(s) from now.".format(18 - votingAge))
else:
    print("Congratulations! You are eligible to cast your vote.")

