#============== CALCULATING AVERAGE IN ARRAY =====================

def calculate_average(numbers): 
    total = 0 
    for num in numbers: 
        total += num
        # += numbers should be num instead
        # number gets added to the each loop
    average = total / len(numbers) 
    # will take the avaergae and divide it by total length
    return average

calculate_average([1,2,3,4])
# numbers need to be in an array

