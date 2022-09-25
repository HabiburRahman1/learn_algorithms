# This function implements the iterative binary search algorithm
def binary_search_iterative(search_list, item):
    # Set the initial values for the lower and upper bounds
    low = 0
    high = len(search_list) -1

    # Loop until the higher bound - lower bound is greater than 1
    while high- low > 1:
        # Calculate the midpoint
        mid = (low + high)//2
        # if item is less than the midpoint, set the upper bound to the midpoint 
        if item < search_list[mid]:
            high = mid
        # if item is greater than the midpoint, set the lower bound to the midpoint
        else:
            low = mid
        # break
    # If the item is found in lower bound, return the index
    if search_list[low] == item:
        return "Item {} found in index {}".format(item, low)
    # If the item is found in higher bound, return the index
    elif search_list[high] == item:
        return "Item {} found in index {}".format(item, high)
    # If the item is not found, return None
    else:
        return "Item not found"

binary_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
searhc_result = binary_search_iterative(binary_list, 10)
print(searhc_result)
