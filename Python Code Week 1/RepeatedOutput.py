#============== REPEATED OUTPUT =====================

# print same word 5x using a loop
for x in range(5):
    print("Olla Amigo\n")
    # will print OLLA AMIGO 5x --> depending on range, output will increase or decrease


#==================================================================#

# as above but with use of FUNCTION
def olla():
    for x in range(10): 
        print("Olla Papi", end = " | ")

#calling the function
olla()