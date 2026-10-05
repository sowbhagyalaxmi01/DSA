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



#***** Implement optimized Bubble Sort. If no swaps happen during a pass, stop the algorithm because the array is already sorted.
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



#Find the second largest element using Bubble Sort
def second_largest(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr[-2]
print(second_largest([4,2,7,1,8]))            


#Find the largest element using only one Bubble Sort pass
def largest(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        break   # stop after the first pass (one complete pass:The largest value 8 has bubbled to the end.)       
    return arr[-1]
print(largest([4,2,7,1,8]))        



#Sort only the first k elements in arr
def second_largest(arr,k):
    for i in range(k):
        for j in range(k-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(second_largest([4,2,7,1,2,8],4)) 



#Sort the even numbers in ascending order, while keeping odd numbers in their original positions.
def even_bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] % 2 == 0:
                k = j + 1
                while k < len(arr):
                    if arr[k] % 2 == 0:
                        if arr[j] > arr[k]:
                            arr[j], arr[k] = arr[k], arr[j]
                        break
                    k += 1
    return arr
print(even_bubblesort([5, 8, 3, 2, 7, 4, 1, 6]))



#*****Number of inversions(An inversion is a pair of numbers where the left number is bigger than the right number) using Bubble Sort
def count_inversions(arr):
    count = 0   # stores the number of inversions
    # Bubble Sort passes
    for i in range(len(arr)):
        # Compare adjacent elements
        for j in range(len(arr) - i - 1):
            # If left element is bigger,
            # they are in the wrong order
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # One inversion is found
                count += 1
    return count
arr = [3, 1, 2]
print(count_inversions(arr))


#****Stop after exactly 2 passes
arr = [9, 7, 5, 3, 1]

# Run Bubble Sort for exactly 2 passes
for i in range(2):

    # Compare adjacent elements
    for j in range(len(arr) - i - 1):

        # Swap if they are in the wrong order
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)

#******1. Sorted array
# 2. Number of swaps
# 3. Number of comparisons
# 4. Number of passes
def bubble_sort(arr):
    swaps = 0
    comparisons = 0
    passes = 0
    for i in range(len(arr)):
        passes += 1
        for j in range(len(arr) - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return arr, swaps, comparisons, passes
arr = [4, 1, 3, 2, 5]
print(bubble_sort(arr))