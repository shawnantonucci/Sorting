# TO-DO: Complete the selection_sort() function below

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        print(smallest_index)
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
               smallest_index = j

        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

        # TO-DO: swap




    print(arr)
    return arr



array_test = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# selection_sort(array_test)

# 1. Loop through your array
#     - Compare each element to its neighbor
#     - If elements in wrong position (relative to each other, swap them)
# 2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

# TO-DO:  implement the Bubble Sort function below

# def swap(arr, a, b):
#     temp = arr[a]
#     arr[a] = arr[b]
#     arr[b] = temp

def bubble_sort(arr):
    complete = False
    while not complete:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                temp = arr[i]
                arr[i] = arr[i -1]
                arr[i - 1] = temp
                swapped = True
        if not swapped:
            complete = True
    return arr

print(bubble_sort(array_test))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

# loop though array
# check siblings
# if index is greater than next sibling
# swap
