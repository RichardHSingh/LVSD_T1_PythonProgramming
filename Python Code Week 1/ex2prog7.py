#============== REVERSED STRING =====================

def reverse_string(s): 
    #parameter is stored as reversed_s
    reversed_s = ""
    for char in s: 
        reversed_s = char + reversed_s 
        # takes first letter and adds to 1st position, then 2nd letter and adds to 1st position
    return reversed_s

reverse_string("hello")
#function wasnt called