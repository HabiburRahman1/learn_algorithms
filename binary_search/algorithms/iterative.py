# This function implements the iterative binary search algorithm
def binary_search_iterative(list_of_integer, item):
    # Set the initial values for the lower and upper bounds
    low = 0
    high = len(list_of_integer) - 1
    # Loop until the lower bound is greater than the upper bound
    while low < high:
        # Calculate the midpoint
        mid = (low + high)//2
        print(mid)
        # If the item is found, return the index
        if item == list_of_integer[mid]:
            return "found the item %s at index %s" % (item, mid)
        # If the item is less than the midpoint, set the upper bound to the midpoint
        elif item < list_of_integer[mid]:
            high = mid
        # If the item is greater than the midpoint, set the lower bound to the midpoint
        else:
            low = mid
    # If the item is not found, return None
    return "item not found"
list_of_integer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(binary_search_iterative(list_of_integer, 1))