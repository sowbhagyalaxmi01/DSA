#Sort the array in ascending order using Selection Sort.
def selection_ascending(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i] 
    return arr
print(selection_ascending([64, 25, 12, 22, 11]))    


#Descending Order
def selection_descending(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]>arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i] 
    return arr
print(selection_descending([5, 2, 8, 1, 9]))    



#Count the number of swaps made by Selection Sort.
# Count the number of swaps made by Selection Sort

def selection_swaps(arr):
    n = len(arr)
    count = 0              # Stores number of swaps
    for i in range(n):
        min_idx = i        # Assume current element is smallest

        # Search for the smallest element
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap only if smallest is at a different position
        if min_idx != i:#only count a swap when a real swap is needed.
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            count += 1     # Count the actual swap
    return count

print(selection_swaps([5, 4, 3, 2, 1])) 


#: Find the k-th smallest element in an array using Selection Sort logic
def selectionsort_kth(arr,k):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i] 
    return arr[k-1]
print(selectionsort_kth([7, 4, 1, 9, 3, 2],3))

# Find the k-th smallest element using Selection Sort
def selectionsort_kth(arr, k):
    n = len(arr)
    # We only need k passes
    for i in range(k):
        # Assume current element is smallest
        min_idx = i
        # Check the remaining elements
        for j in range(i + 1, n):
            # If a smaller element is found
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Put the smallest element at position i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # k-th smallest is at index k-1
    return arr[k - 1]

print(selectionsort_kth([7, 4, 1, 9, 3, 2], 3))


#Given an array and k, find the k-th largest element using Selection Sort logic.
def selectionsort_kth_largest(arr, k):
    n = len(arr)
    for i in range(k):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr[k - 1]
print(selectionsort_kth_largest([7, 4, 1, 9, 3, 2], 2))