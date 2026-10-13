
def merge_sort(arr):
    # Divide only if the list has more than one element
    if len(arr) > 1:

        # Find the middle
        mid = len(arr) // 2

        # Split into left and right lists
        L = arr[:mid]
        R = arr[mid:]

        # Sort both lists
        merge_sort(L)
        merge_sort(R)

        # i = left index, j = right index, k = original list index
        i = j = k = 0

        # Compare elements from both lists
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy remaining elements from the left list
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy remaining elements from the right list
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


arr = [45, 32, 76, 32, 12, 56]
merge_sort(arr)
print(arr)
