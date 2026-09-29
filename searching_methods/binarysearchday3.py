#Binary Search is a searching algorithm used to find a target element in a sorted array/list(half by half).
#**The array must be sorted.Binary Search doesn't search every element. It keeps cutting the search area in half.
#Time complexity: O(log n)

# ALGORITHM
# 1.intialize low=0,high=len(arr)-1.
# 2.find middle element:mid=(low+high)//2.
# 3.compare middle element with target:both are equal,return Idx.
# 4.if target>middle element:search right half and update low=mid+1.
# 5.if target <middle element:search left and update high=mid-1.
# 6.repaet until element is found or low>high.
# 7.if not found return -1.


#code
def binary_search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1
print(binary_search([3,7,8,9,14,16,17,22,24],8))     


#problems
#1. Find Target Index
# arr = [2, 5, 8, 12, 16, 20]
# target = 12
# Return the index of target.
def binary_search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
print(binary_search([2, 5, 8, 12, 16, 20],12))         


#Target Not Found
# arr = [3, 7, 10, 15, 20]
# target = 8
# Return -1.
def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
print(binary_search([3, 7, 10, 15, 20],8))            


#Find Number
# arr = [1, 4, 6, 9, 12, 15]
# target = 9
# Return the number itself if found, otherwise -1.
def binary_search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return arr[mid]
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1 
print(binary_search( [1, 4, 6, 9, 12, 15],9))   


#4. Check if Target Exists
# arr = [2, 4, 6, 8, 10, 12]
# target = 10
def target_exists(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return True
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return False
print(target_exists([2, 4, 6, 8, 10, 12],10))


#6. Find Middle Element
# arr = [2, 4, 6, 8, 10, 12, 14]
# Use binary-search-style mid calculation to find the middle element.
def middle_ele(arr):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        return arr[mid]
print(middle_ele([2, 4, 6, 8, 10, 12, 14]))


#7. Search Insert Position
# arr = [1, 3, 5, 6]
# target = 5
# Expected:2
# Then try:
# target = 2
# Expected:1
def search_insert(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low
print(search_insert([1, 3, 5, 6], 5))
print(search_insert([1, 3, 5, 6], 2))


#8.Find First Occurrence
# arr = [1, 2, 2, 2, 3, 4]
# target = 2
# Return the first index of 2.
def first_occurrence(arr, target):

    low = 0                  # First index
    high = len(arr) - 1      # Last index
    answer = -1              # Target not found yet

    while low <= high:

        mid = (low + high) // 2   # Find middle index

        if arr[mid] == target:
            answer = mid           # Target found, save index
            high = mid - 1         # Go LEFT to find an earlier target

        elif arr[mid] < target:
            low = mid + 1          # Target is on the RIGHT

        else:
            high = mid - 1         # Target is on the LEFT

    return answer                  # Return first occurrence
print(first_occurrence([1, 2, 2, 2, 3, 4], 2))


#9. Find Last Occurrence
# arr = [1, 2, 2, 2, 3, 4]
# target = 2
# Expected:3
def last_occurrence(arr, target):

    low = 0                  # First index
    high = len(arr) - 1      # Last index
    answer = -1              # Target not found yet

    while low <= high:

        mid = (low + high) // 2   # Find middle index

        if arr[mid] == target:
            answer = mid           # Target found, save index
            low = mid + 1          # Go RIGHT to find a later target

        elif arr[mid] < target:
            low = mid + 1          # Target is on the RIGHT

        else:
            high = mid - 1         # Target is on the LEFT

    return answer                  # Return last occurrence
print(last_occurrence([1, 2, 2, 2, 3, 4], 2))


#10.Count Occurrences
# arr = [1, 2, 2, 2, 3, 4]
# target = 2
# Expected:3
def count_occurrences(arr, target):

    # Find first occurrence
    low = 0
    high = len(arr) - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            first = mid
            high = mid - 1       # search left
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # If target is not present
    if first == -1:
        return 0

    # Find last occurrence
    low = 0
    high = len(arr) - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            last = mid
            low = mid + 1        # search right
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # Count = last index - first index + 1
    return last - first + 1
print(count_occurrences([1, 2, 2, 2, 3, 6], 2))


#11.Find Peak Element
# arr = [1, 3, 5, 7, 6, 4, 2]
# Return the index of the peak element.
# Expected:3
def find_peak(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low
print(find_peak([1, 3, 5, 7, 6, 4, 2]))


# 12.Find Minimum in Rotated Sorted Array
# arr = [4, 5, 6, 7, 0, 1, 2]
# Expected:0
def find_min(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            low = mid + 1      # minimum is RIGHT
        else:
            high = mid       #  minimum is LEFT or MID

    return arr[low]


print(find_min([4, 5, 6, 7, 0, 1, 2]))

# 13.Search in Rotated Sorted Array
# arr = [4, 5, 6, 7, 0, 1, 2]
# target = 0
# Expected:4
def find_min(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid

    return arr[low]


print(find_min([4, 5, 6, 7, 0, 1, 2]))


# 14.
# Find Single Element
# Every number appears twice except one:
# arr = [1, 1, 2, 2, 3, 4, 4, 5, 5]
# Expected:3
# Because 3 appears only once.
def single_element(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if mid % 2 == 1:
            mid -= 1

        if arr[mid] == arr[mid + 1]:
            low = mid + 2
        else:
            high = mid

    return arr[low]


print(single_element([1, 1, 2, 2, 3, 4, 4, 5, 5]))



#count freq of each unique word inside txt sentence
sentence = input("Enter a sentence: ")#cat dog cat
words = sentence.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
count=0
for word in freq:
    if freq[word]==1:
        count+=1
print("count:",count)        