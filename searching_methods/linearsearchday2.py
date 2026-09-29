#linear search is used when the given array is unsorted.
#time complexity:0(n)

# Algorithm Steps:

# Start from the first element of the array.
# Compare the current element with the target value.
# If both are equal, return the position/index.
# Otherwise, move to the next element.
# Repeat until the element is found or the array ends.
# If the array ends and the element is not found, return -1.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:#return index of target 
            return i
    return -1
print(linear_search([12, 34, 11, 67, 54], 11))


#Find the Number
# Return the target number itself if found.
# Otherwise return -1.
def linear_search(arr,target):
    for num in arr:
        if num==target:
            return num
    return -1
print(linear_search([12, 34, 11, 67, 54], 67))   


#Check if Number Exists
# Return True if target exists, otherwise False.
def linear_search(arr,target):
    for num in arr:
        if num==target:
            return True
    return False
print(linear_search([12, 34, 11, 67, 54], 67))   


#Find First Occurrence
# Find the first index where the target appears.
# Example: [2, 4, 2, 7], target 2 → 0.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target: 
            return i#return i already stops the function when the first occurrence is found.no need of break(stop the loop)
    return -1
print(linear_search([2,4,2,7], 2))


# Count Occurrences
# Count how many times the target appears.
# Example: [2, 4, 2, 2], target 2 → 3.
def count_occurances(arr,target):
    count=0
    for num in arr:
        if num==target:
            count+=1
    return count
print(count_occurances([2,4,2,2],2))


#Find Maximum
# Find the largest number using a linear scan.
def maximum(arr):#Your code checks each element one by one:so it is a linear scan/search-type problem.
    maximum=arr[0]
    for num in arr:
        if num>maximum:
            maximum=num
    return maximum
print(maximum([2,4,2,6,3]))



# Find Minimum
# Find the smallest number using a linear scan.
def minimum(arr):#Your code checks each element one by one:so it is a linear scan/search-type problem.
    minimum=arr[0]
    for num in arr:
        if num<minimum:
            minimum=num
    return minimum
print(minimum([7,4,2,6,3]))

#Find All Occurrences
# Return all indexes where the target appears.
# Example: [5, 2, 5, 7, 5], target 5 → [0, 2, 4].
def target_occurances(arr,target):
    result=[]
    for i in range(len(arr)):
        if arr[i]==target:
            result.append(i)
    return result   
print(target_occurances([5,2,5,7,5],5))

# Find Second Largest
# Find the second-largest number using one pass.
def second_largest(arr):
    largest=arr[0]
    second=arr[0]
    for num in arr:
        if num>largest:
            second=largest
            largest=num
        elif num>second and num<largest:
            second=num    
    return second        
print(second_largest([5,2,9,7,1]))
# Search in a String
# Find the first occurrence of a character.
# Example: "hello", target "l" → 2
def str_occurrences(s, target):
    for i in range(len(s)):
        if s[i] == target:
            return i
    return -1
print(str_occurrences("hello", "l"))   
       

# Find Duplicate
# Find whether an array contains a duplicate.
def duplicates(arr):
    return len(arr)==len(set(arr))
print(duplicates([23,36,34,87,65,87]))


# Find Missing Number
# Given numbers from 1 to n with one missing, find the missing number.
def missing_number(arr):
    n = len(arr) + 1
    for num in range(1, n + 1):
        if num not in arr:
            return num
print(missing_number([1, 2, 3, 5]))

        