# #Counting Sort — Easy Explanation
# Counting Sort is a sorting algorithm that counts how many times each number appears and then uses those counts to sort the array.
# Unlike Bubble Sort, it does not compare two numbers to decide which is smaller.


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
def counting_sort(arr):#[4, 2, 2, 8, 3, 3, 1]
    max_val = max(arr)#8
    count = [0] * (max_val + 1)#[0,0,0,0,0,0,0,0,0] -->[0,1,2,2,1,0,0,0,1]

    # Count frequency
    for i in arr:#
        count[i] += 1

    # Place elements back into arr
    j = 0#represent idx of org array
    for i in range(len(count)):#i takes val from count
        while count[i] > 0:
            arr[j] = i
            j += 1
            count[i] -= 1
    return arr#[1,2,2,3,3,4,8]
arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))


#2. Why Not Counting Sort?(drawbacks)
# It is not suitable when the range of values is very large.
# It requires extra memory for the count array.
# The basic implementation does not directly handle negative numbers.
# It is not suitable for directly sorting decimal or floating-point values.
# It is less efficient when the range of values is much larger than the number of elements.
# It is not ideal for general-purpose sorting when the input range is unknown or extremely large.