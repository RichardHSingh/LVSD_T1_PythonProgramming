#============== EXERCISE WHO IS OLDER ====================

# finding out who is older out of given age inpout

print("Who is older out StretchMan or NinjaBoy.\n")

# Get StretchMan's age
StretchManAge = int(input("StretchMan enter your age: "))


# Get NinjaBoy's age
NinjaBoyAge = int(input("NinjaBoy enter your age: "))


# Check who is older using if statements
if StretchManAge > NinjaBoyAge:
    print("StretchMan is older than NinjaBoyAge by " + str(StretchManAge - NinjaBoyAge) + " years.")
elif StretchManAge == NinjaBoyAge:
    print("You are both the same age.")
else:
    print("StretchMan is younger than NinjaBoyAge.")


    