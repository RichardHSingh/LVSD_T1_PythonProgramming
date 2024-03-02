#============== GUESSING GAME =====================

# guessing game for when user imputs number and has 3 chances of getting it correct

# using right click "rename" or F2, one can rename the variable or anything in python
# and this will rename everywhere this symbol or word is being used

# in python, while loops can have else statements in it

secret_number = 8
# number that user is trying to guess is stated above

guess_count = 0
# x = the number of guessing one can have which is less than 3

guess_limit = 3
# instead of defining a random number in condition, using variable name and its value

while guess_count < guess_limit:
    guess = int(input("\nGuess a number between 0 and 10:"))
    guess_count += 1

    if guess == secret_number:
        print("\nCongratulations! YOU WON!")
        break
    # break terminates the loop like in c#

else:
    print("\nOOPSIES! You ran out of guesses!")


