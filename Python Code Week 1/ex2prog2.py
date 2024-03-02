#============== FACTORIAL OF GIVEN NUMBER =====================

def factorial(n): 
    if n == 0 or n == 1: 
        return 1 
    else: 
        return n * factorial(n-1)

factorial(5)
# factorial means to take a number and multiply by numbers that precede it

