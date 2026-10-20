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