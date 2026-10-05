#Selection Sort selects the smallest element from the unsorted list and places it at the beginning.
#Time Complexity: O(n²)
#****Select the minimum element and place it in its correct position.


#ALGORITHM:
# 1.Assume the first element is the minimum.
# 2.Compare it with all remaining elements.
# 3.Find the smallest element in the unsorted part.
# 4.Swap the smallest element with the first unsorted position.
# 5.Move the boundary of the sorted part by one position.
# 6.Repeat for the remaining unsorted elements.
# 7.Continue until the entire array becomes sorted.


def selection_sort(arr):
    n = len(arr)  # Find the length of the array

    for i in range(n):
        # Assume the current position has the smallest element
        min_idx = i

        # Search for a smaller element in the remaining array
        for j in range(i + 1, n):
            # If we find a smaller element
            if arr[j] < arr[min_idx]:
                min_idx = j  # Store its index

        # Swap the smallest element with arr[i]
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
arr = [5, 3, 4, 1, 2]
print(selection_sort(arr))