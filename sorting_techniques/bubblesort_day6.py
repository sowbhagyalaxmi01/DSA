#using while loop
def bubble_sort(arr):
    n = len(arr)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        i += 1
    return arr
print(bubble_sort([5, 3, 8, 1]))



#PROBLEMS
#1.Given an array of integers, sort the array in ascending order using Bubble Sort.(arr = [5, 3, 8, 4, 2])
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort( [5, 3, 8, 4, 2]))


#Given an array of integers, sort the array in descending order using Bubble Sort.
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort([4, 1, 7, 3, 9]))


#Given an array that may already be sorted, use Bubble Sort to sort it in ascending order.
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort( [1, 2, 3, 4, 5]))



#Perform only the first complete pass of Bubble Sort(only 1st pass)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        break        
    return arr
print(bubble_sort([5, 1, 4, 2, 8]))


#Write a program to count how many swaps Bubble Sort performs while sorting the array
def bubble_sort(arr):
    count=0
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
#1.Given an array of integers, sort the array in ascending order using Bubble Sort.(arr = [5, 3, 8, 4, 2])
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort( [5, 3, 8, 4, 2]))


#Given an array of integers, sort the array in descending order using Bubble Sort.
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort([4, 1, 7, 3, 9]))


#Given an array that may already be sorted, use Bubble Sort to sort it in ascending order.
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort( [1, 2, 3, 4, 5]))



#Perform only the first complete pass of Bubble Sort(only 1st pass)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        break        
    return arr
print(bubble_sort([5, 1, 4, 2, 8]))


#Write a program to count how many swaps Bubble Sort performs while sorting the array
def bubble_sort(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1#increse count only when swap happens.(if count below if stmt count increases even when there is no swap.)
    return count
print(bubble_sort([3, 2, 1]))


#Given an array of integers, use Bubble Sort and find the number of passes required to completely sort the array in ascending order.
def bubble_sort(arr):
    passes = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        passes+=1 #checking only 1 pass, then the j loop tells us how many comparisons happen in that one pass.           
    return passes
print(bubble_sort([3, 2,7, 1]))



# Implement optimized Bubble Sort. If no swaps happen during a pass, stop the algorithm because the array is already sorted.
# optimized  bubble sort:Normal Bubble Sort keeps doing passes even if the array is already sorted.
def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr
print(bubble_sort([1, 2, 3, 4, 5]))


def bubble_sort(arr):
    for i in range(len(arr)):
        count = 0  # Reset count for every new pass
        for j in range(len(arr) - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if left element is bigger
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1  # Increase count only when swap happens
        # If no swap happened in this pass, array is sorted
        if count == 0:
            break
    return arr
print(bubble_sort([5, 1, 4, 2, 8]))


#Sort an array containing both positive and negative numbers using Bubble Sort.
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort([3, -1, 4, -5, 2]))
