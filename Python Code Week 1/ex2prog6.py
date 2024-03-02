#============== BIGGEST ELEMENT IN ARRAY =====================

def find_max(numbers): 
    # starting array from bottom to give accurate output
    max_num = 0
    for num in numbers: 
        if num > max_num:
            # max_num was called nor was num for what to compare it to
            max_num = num 
     # returning loop   
    return max_num

# searching through array for biggest element
find_max([1,2,3,4])
