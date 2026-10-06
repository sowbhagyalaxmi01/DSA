# Insertion Sort
# Insertion Sort builds the sorted list one element at a time.
# Time Complexity: O(n²)

                   
# Algorithm Steps:
# Consider the first element as already sorted.
# Pick the next element (called Key).
# Compare the Key with elements on its left.
# Shift all larger elements one position to the right.
# Insert the Key into its correct position.
# Move to the next element.
# Repeat until all elements are inserted into their correct positions.



def insertion_sort(arr):

    # Start from second element
    for i in range(1, len(arr)):

        # Current element
        key = arr[i]

        # Previous element
        j = i - 1

        # Shift bigger elements to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key in correct position
        arr[j + 1] = key
    return arr    
# Function call
print(insertion_sort( [5, 3, 4, 1]))
