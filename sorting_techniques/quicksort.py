#Quick Sort is also divide and conquer. It picks a pivot element and partitions. 
#the array into two — elements smaller than pivot and greater than pivot — then sorts them recursively.
#Time Complexity: O(n log n) average, O(n²) worst.

#ALGORITHM
# Choose a pivot element.
# Compare other elements with the pivot.
# Move smaller elements to the left and larger elements to the right.
# Place the pivot in its correct position.
# Repeat the process for the left and right parts.
# Stop when a part has zero or one element.


#POINTS
# Quick Sort is a divide-and-conquer sorting algorithm.
# Pivot is the element chosen to partition the array.
# Elements smaller than or equal to the pivot go to the left; larger elements go to the right.
# After partitioning, the pivot reaches its correct sorted position.
# Quick Sort recursively sorts the left and right subarrays.
# Base condition: If the array has 0 or 1 element, it is already sorted.
# Best-case time complexity: \(O(n\log n)\).
# Average-case time complexity: \(O(n\log n)\).
# Worst-case time complexity: \(O(n^2)\).
# Auxiliary space complexity: typically \(O(\log n)\) for balanced recursive partitions in an in-place implementation; it can reach \(O(n)\) in the worst case.
# Quick Sort is generally not stable
# It is usually an in-place algorithm when implemented using partitioning, without creating separate left and right lists.


# code:
# Quick Sort

def quick_sort(arr):

    n = len(arr)  # Find the number of elements

    # Base condition: 0 or 1 element is already sorted
    if n <= 1:
        return arr

    # Choose the middle element as pivot
    pivot = arr[n // 2]

    left = []    # Store elements smaller than pivot
    middle = []  # Store elements equal to pivot
    right = []   # Store elements greater than pivot

    # Compare each element with the pivot
    for x in arr:

        if x < pivot:
            left.append(x)   # Add smaller elements to left

        elif x == pivot:
            middle.append(x) # Add pivot elements to middle

        else:
            right.append(x)  # Add greater elements to right

    # Sort left and right recursively, then combine all lists
    return quick_sort(left) + middle + quick_sort(right)


# Main program
a = [8, 6, 4, 9, 1, 2]

print(quick_sort(a))g
