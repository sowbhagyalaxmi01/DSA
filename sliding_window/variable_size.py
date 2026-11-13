# Variable-Size Sliding Window
# Variable-Size Sliding Window is a technique where the window size increases or decreases depending on a given condition.


# Algorithm
# 1. Initialize left = 0.
# 2. Initialize window_sum = 0.
# 3. Initialize min_length = infinity.
# 4. Move the right pointer through the array.
# 5. Add the current element to window_sum.
# 6. While window_sum >= target:
#    - Update the minimum length.
#    - Remove the leftmost element.
#    - Move left forward.
#7. Return the minimum length.



#code
# Input array
nums = [2, 3, 1, 2, 4, 3]
target = 7

# Initialize pointers and variables
left = 0
window_sum = 0
min_length = float('inf')

# Traverse the array
for right in range(len(nums)):

    # Add current element to window
    window_sum += nums[right]

    # Shrink window while condition is satisfied
    while window_sum >= target:

        # Update minimum subarray length
        min_length = min(min_length, right - left + 1)

        # Remove leftmost element
        window_sum -= nums[left]

        # Move left pointer
        left += 1

# Print result
if min_length == float('inf'):
    print(0)
else:
    print(min_length)