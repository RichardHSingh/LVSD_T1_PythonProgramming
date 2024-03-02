#============== PRINTING STRINGS =====================

# print first line
x = "Sean is the best TA we have had in SD :)"

# print second line
y = "ZOHEB for CLASS REP WHOOP WHOOP"

# \n is same as C# and it works so yea
print(x,"\n" +y)


#==================================================================#

# as above but utilising function instead
def multiLine():
    line1 = "Sean is the best TA we have had for SD course"
    line2 = "ZOHEB for class REP WHOOP WHOOP!"
    print(f"{line1} \n{line2}")

#calling function
multiLine()

