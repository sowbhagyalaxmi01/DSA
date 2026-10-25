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


arr = [3, 3, 2, 4]
print(counting_sort(arr))