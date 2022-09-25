def binary_search_iterative(search_list, item):
    low = 0
    high = len(search_list) -1

    while high- low > 1:
        mid = (low + high)//2
        if item < search_list[mid]:
            high = mid
        else:
            low = mid
        # break
    if search_list[low] == item:
        return "Item {} found in index {}".format(item, low)
    elif search_list[high] == item:
        return "Item {} found in index {}".format(item, high)
    else:
        return "Item not found"

binary_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
searhc_result = binary_search_iterative(binary_list, 10)
print(searhc_result)
