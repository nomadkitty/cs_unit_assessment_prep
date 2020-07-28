# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # loop: compare current_index > current_index +1. swap
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr)-i-1):
            current_index = j
            next_index = j + 1
            if arr[current_index] > arr[next_index]:
                arr[current_index], arr[next_index] = arr[next_index], arr[current_index]

    # Matt's solution
    # swaps_occurred = True
    # while swaps_occurred:
    #     swaps_occurred = False
    #     for i in range(0, len(arr)-1):
    #         if arr[i] > arr[i+1]:
    #             # swap
    #             arr[i], arr[i+1] = arr[i+1], arr[i]
    #             swaps_occurred = True

    return arr
