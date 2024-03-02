#============== CHECKING N IS PRIME OR NOT =====================

def is_prime(n): 
    prime = True 

    
    for i in range(2, n): 
        #loops checks that given number divisible any number = not prime return false
        if n % i == 0: 
            prime = False 

    return prime

is_prime(9)
# declare parameter to check if its prime
# true = prime, flase = not prime

