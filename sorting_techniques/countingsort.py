# #Counting Sort — Easy Explanation
# Counting Sort is a sorting algorithm that counts how many times each number appears and then uses those counts to sort the array.
# Unlike Bubble Sort, it does not compare two numbers to decide which is smaller.

#points
# Counting Sort is a non-comparison sorting algorithm.
# It sorts elements by counting the frequency of each value.
# It uses an additional array called the count array.
# It works best when the range of input values is small.
# It is mainly used for sorting integers.
# It does not compare elements with each other.
# Time Complexity: \(O(n+k)\).
# Space Complexity: \(O(n+k)\) in the standard implementation.
# It is efficient for small ranges of values.
# It requires extra memory for counting.

def counting_sort(arr):
    # Find the largest number
    maximum = max(arr)

    # Create a count array filled with zeros
    count = [0] * (maximum + 1)

    # Count how many times each number appears
    for num in arr:
        count[num] += 1

    # Create the sorted array
    result = []

    # Add each number according to its count
    for num in range(len(count)):
        for i in range(count[num]):
            result.append(num)

    return result
arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))


#second code
def counting_sort(arr):
    max_val = max(arr)
    count = [0]*(max_val+1) #[0 0 1 2 1]
                            # 0 1 2 3 4

    for num in arr: #3 3 2 4
        count[num]+=1

    j= 0
    for i in range(len(count)): #0
        while count[i]>0:
            arr[j] = i
            j+=1
            count[i]-=1
    return arr
a = [8,6,4,9,1,2]
b= [3, 3, 2, 4]
print(counting_sort(a)) 
print(counting_sort(b))             



#2. Why Not Counting Sort?(drawbacks)
# It is not suitable when the range of values is very large.
# It requires extra memory for the count array.
# The basic implementation does not directly handle negative numbers.
# It is not suitable for directly sorting decimal or floating-point values.
# It is less efficient when the range of values is much larger than the number of elements.
# It is not ideal for general-purpose sorting when the input range is unknown or extremely large.