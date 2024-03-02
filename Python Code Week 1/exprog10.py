#============== PRBLEM SOLVING =====================

# CALCULATING AVERAGE IN ARRAY
def find_average(nums): 
    total = 0 
    count = 0 

# looping through list to count num of element and divid by how many elements there are
    for num in nums: 
        total += num 
        count += 1 
        # was =+ rather than +=
    average = total / count 
    return average

find_average([1,2,3,4,5])
# need to use list/array for calculation

