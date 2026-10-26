# Stable Counting Sort
# 1. Definition
# Stable Counting Sort is a sorting algorithm that sorts elements based on their frequency and preserves the relative order of equal elements in the original array.
# It is a non-comparison-based sorting algorithm because it does not compare elements with each other.
# time complexity:O(n+k)
# Counting frequencies → O(n)
# Creating cumulative counts → O(k)
# Building output → O(n)


# To achieve stability, Counting Sort performs two additional steps:
# Convert the count array into a cumulative (prefix sum) array.
# Traverse the original array from right to left and place each element into its correct position in the output array.


# Algorithm
# 1. Find the maximum element.
# 2. Create a count array of size (max + 1).
# 3. Initialize all counts to 0.
# 4. Count the frequency of each element.
# 5. Convert the count array into cumulative counts (for stable version).
# 6. Traverse the input array from right to left.
# 7. Place each element into the output array using the cumulative count


def counting_sort(arr):

    max_val = max(arr)

    # Step 1: Create count array
    count = [0] * (max_val + 1)

    # Step 2: Count frequency of each number
    for num in arr:
        count[num] += 1
    # Step 3: Calculate cumulative counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 4: Create output array
    output = [0] * len(arr)

    # Step 5: Traverse the original array from right to left
    for j in reversed(arr):

        # Place the number at its correct position
        output[count[j] - 1] = j

        # Decrease count to get the previous position
        count[j] -= 1

    return output


arr = [4,2,2,8,3,3,1]
print(counting_sort(arr))