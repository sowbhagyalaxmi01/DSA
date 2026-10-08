#Sort an array in ascending order
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move larger elements to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Put key in the correct position
        arr[j + 1] = key
    return arr
arr = [5, 2, 4, 1, 3]
print(insertion_sort(arr))



#. Descending order
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move sma
        # ller elements to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        # Put key in the correct position
        arr[j + 1] = key
    return arr
arr = [5, 2, 4, 1, 3]
print(insertion_sort(arr))