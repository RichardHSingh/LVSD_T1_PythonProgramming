#============== CODD N' EVEN =====================

# Checking if entered number is odd or even

# Asking user to enter a number
num = int(input("Please enter a number: "))

# Checking if the entered number is even
if num % 2 == 0:
    print("Number you have entered is {} - this number has an even value".format(num))
else:
    print("Number you have entered is {} - this number has an odd value".format(num))

# Pausing execution to see the result
input()

# If the number is divisible by 2, it is even; otherwise, it is odd
# .format changes the number to a string which allows number to be put into print

