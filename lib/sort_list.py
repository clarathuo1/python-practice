#Sorts a list of tuples by age in ascending order.

def sort_by_age(tuples_list):
    
    #Returns list which is the sorted list of tuples

    return sorted(tuples_list, key=lambda x: x[1])