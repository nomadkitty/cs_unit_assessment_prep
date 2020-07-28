# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # compare [0] index of both arr the smaller one replace merged_arr index position
    for i in range(len(merged_arr)):
        # handle edge case of when len of either arr is 0
        if len(arrA) == 0 or len(arrB) == 0:
            return merged_arr[:i] + arrA + arrB
        if arrA[0] <= arrB[0]:
            merged_arr[i] = arrA[0]
            arrA = arrA[1:]
        else:
            merged_arr[i] = arrB[0]
            arrB = arrB[1:]

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    # base case: if len(arr) <=1 return arr
    if len(arr) <= 1:
        return arr
    # recursively divide arr to left arr and right arr
    # pass them into helper funcition
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    arrA = merge_sort(left)
    arrB = merge_sort(right)
    arr = merge(arrA, arrB)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
