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
# 7. Return the minimum length.