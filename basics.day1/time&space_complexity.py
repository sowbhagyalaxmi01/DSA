# Time and Space Complexity

# Time complexity measures how the runtime of an algorithm grows with input size.
# Space complexity measures how much memory it requires.
# We usually express complexity using Big O notation:
# -Big OsO(1) Constant- no loops
# -O(log N) Logarithmic- usually searching algorithms have log n if they are sorted (Binary Search)
# -O(n) Linear- for loops, while loops through n items
# -O(n log(n)) Log Liniear- usually sorting operations
# -O(n^2) Quadratic- every element in a collection needs to be compared to ever other element. Two nested loops
# -O(2^n) Exponential- recursive algorithms that solves a problem of size N
# -O(n!) Factorial- you are adding a loop for every element


# 1. O(1) — Constant
# The work stays the same regardless of n.
arr = [10, 20, 30, 40, 50]
print(arr[0])
# Only one element is accessed.
# Time → O(1)
# Extra Space → O(1)
# Real world
# You have 1,000 books or 1,000,000 books, but you directly access book #5.


# 2. O(n) — Linear
# The work increases with the number of elements.
arr = [10, 20, 30, 40, 50]
for x in arr:
    print(x)
# If:
# n = 5       → 5 operations
# n = 100     → 100 operations
# n = 1000    → 1000 operations
# So:
# Time → O(n)
# Real world
# Checking every student in a class to find a particular student.


# 3. O(n²) — Quadratic
# Usually happens when we have a loop inside another loop.
arr = [1, 2, 3, 4]
for i in arr:
    for j in arr:
        print(i, j)
# For n = 4:
# 4 × 4 = 16
# For n = 100:
# 100 × 100 = 10,000
# So:
# Time → O(n²)

# Real world
# Suppose 4 students each need to interact with every student:
# 4 × 4 = 16 interactions


# 4. O(log n) — Logarithmic
# The input is reduced significantly at every step.
# Binary Search is the common example.
# Suppose we have:
# 1 2 3 4 5 6 7 8
# To find 7:
# Check middle → 4
# 7 is bigger → ignore left half
# Check middle → 6
# 7 is bigger → ignore left half
# Check → 7
# Found
# Instead of checking every element, we keep cutting the search area in half.
# Time → O(log n)


# Space Complexity
# O(1) Space
# a = 10
# b = 20
# c = a + b
# Only a few variables are created.
# Space → O(1)

# O(n) Space(new arr created)
# arr = []
# for i in range(5):
#     arr.append(i)
# If n = 5:
# [0, 1, 2, 3, 4]
# If n = 1000, the list stores 1000 elements.
# So:
# Space → O(n)