#============== CALCULATION WATERFALL PATTERN =====================

def print_pattern(rows): 
    #for loop loops though each row
    for i in range(1, rows + 1): 
        # j is the columns in that row
        for j in range(1, i + 1) :
            print(j, end=" ") 
            # j needs to outside the double quote

        print()
        # if this print isnt here, everything will print in one line
        # but we want to print new row each time

print_pattern(4)
# function name was wrong
# oddly still prints 1 row less than stated number


