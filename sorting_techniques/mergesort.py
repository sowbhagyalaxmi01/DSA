#first code
def merge_sort(arr):
    # Base case: if array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle position
    mid = len(arr) // 2

    # Recursively sort the left half
    left = merge_sort(arr[:mid])

    # Recursively sort the right half
    right = merge_sort(arr[mid:])

    # Create an empty list to store sorted elements
    result = []

    # i is the index of left; j is the index of right
    i = j = 0

    # Compare elements while both lists have elements
    while i < len(left) and j < len(right):

        # If left element is smaller or equal
        if left[i] <= right[j]:
            result.append(left[i])  # Add left element
            i += 1                  # Move to next left element

        else:
            result.append(right[j]) # Add right element
            j += 1                  # Move to next right element

    # Add any remaining elements from the left list
    result.extend(left[i:])

    # Add any remaining elements from the right list
    result.extend(right[j:])

    # Return the fully sorted array
    return result

arr = [6, 4, 3, 2, 7, 1]
print(merge_sort(arr))




#alternate code
def merge_sort(arr):
    # Divide only if the list has more than one element
    if len(arr) > 1:

        # Find the middle
        mid = len(arr) // 2

        # Split into left and right lists
        L = arr[:mid]
        R = arr[mid:]

        # Sort both lists
        merge_sort(L)
        merge_sort(R)

        # i = left index, j = right index, k = original list index
        i = j = k = 0

        # Compare elements from both lists
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy remaining elements from the left list
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy remaining elements from the right list
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

arr = [45, 32, 76, 32, 12, 56]
merge_sort(arr)
print(arr)






