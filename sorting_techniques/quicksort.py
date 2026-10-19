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