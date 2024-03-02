#============== CHRISTMS TREE =====================

# while loops is to execute a block of code multiple times
# often used in interactive programs and/or games
# written as --> while condition: and while is true will perform code associated with it
# if you dont state increment x = x + 1, the loop becomes infinate and will never end as 1 is <= 10

x = 1

while x <= 10:
    print('*' * x)
    x = x + 1
print("\nCompleted")
# this code will display number of * associated with the number that is being looped
# * when x = 1 or *** when x is = 3