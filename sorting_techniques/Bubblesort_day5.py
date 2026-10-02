
# Binary Search works on sorted lists. It repeatedly divides the search interval in half.
# Time Complexity: O(log n)
#The array must be sorted.

# Algorithm Steps:

# Initialize:
# low = 0
# high = n - 1
# Find the middle element:
# mid = (low + high) // 2
# Compare the middle element with the target.
# If both are equal, return the index.
# If the target is greater than the middle element:
# Search the right half.
# Update low = mid + 1
# If the target is smaller than the middle element:
# Search the left half.
# Update high = mid - 1
# Repeat until the element is found or low > high.
# If not found, return -1.


#code:
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr=list(map(int,input().split()))
print(bubble_sort(arr))


