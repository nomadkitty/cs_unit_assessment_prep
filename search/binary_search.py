# Write an iterative implementation of Binary Search
def binary_search_iterative(arr, target):
    # Your code here
    start_index = 0
    end_index = len(arr) - 1

    while start_index <= end_index:
        middle_index = (start_index + end_index)//2
        if arr[middle_index] == target:
            return middle_index
        if arr[middle_index] > target:
            end_index = middle_index - 1
        else:
            start_index = middle_index + 1

    return -1  # not found


# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # base case: if arr[middle] == target
    middle = (start + end) // 2
    if middle >= 0 and arr[middle] == target:
        return middle
    # recursive: guess the middle
        # if arr[middle] > target:
        # change end to middle -1
    if middle >= 0 and arr[middle] > target:
        return binary_search(arr, target, start, middle-1)
    if middle >= 0 and arr[middle] < target:
        return binary_search(arr, target, middle+1, end)
    else:
        return -1
