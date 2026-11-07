# Fixed-size Sliding Window Algorithm
# Definition: A fixed-size Sliding Window maintains a window of exactly K elements while moving through an array or string.

g
# Algorithm steps:
# 1. Initialize the window size K.
# 2. Calculate the sum of the first K elements.
# 3. Store the initial result.
# 4. Move the window one position to the right.
# 5. Add the new element entering the window.
# 6. Remove the old element leaving the window.
# 7. Update the maximum or minimum result.
# 8. Repeat until the array ends.



#code
# Given array
nums = [2, 1, 5, 1, 3, 2]

# Window size
k = 3

# Calculate sum of first 3 elements
window_sum = sum(nums[:k])

# Initially, maximum sum is the first window sum
max_sum = window_sum

# Start loop from index k
for right in range(k, len(nums)):

    # Add the new element entering the window
    window_sum += nums[right]

    # Remove the old element leaving the window
    window_sum -= nums[right - k]

    # Update maximum sum
    max_sum = max(max_sum, window_sum)

# Print final maximum sum
print(max_sum)