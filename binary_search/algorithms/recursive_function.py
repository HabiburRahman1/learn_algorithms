
def binary_search_recusive(array, target, start, end):
    if start >= end:
        return "Not found in array"
    mid = (start + end) // 2
    if array[mid] == target:
        return "Found {} at index {}".format(target,mid)
    elif array[mid] > target:
        return binary_search_recusive(array, target, start, mid)
    else:
        return binary_search_recusive(array, target, mid + 1, end)

if __name__ == "__main__":
    search_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 5
    print(binary_search_recusive(search_list, target, 0, len(search_list)))