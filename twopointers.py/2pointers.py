#Two pointers is a technique that uses two variables to track positions in an array or string to solve problems efficiently.
#Pointers can start at opposite ends and move toward each other, or move in the same direction, depending on the problem.
#two pointers used to reduce time complexity
#two pointers used for only sorted array


#To reverse array
arr=list(map(int,input().split()))
left=0
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(arr)    


#two sum pointer
arr = list(map(int, input().split()))
target = int(input())

left = 0
right = len(arr) - 1

while left < right:
    total = arr[left] + arr[right]

    if total == target:
        print(arr[left], arr[right])
        left += 1
        right -= 1
    elif total < target:
        left += 1
    else:
        right -= 1


#string palindrome or not ---->
s = "madam"

l = 0
r = len(s) - 1

while l < r:
    if s[l] == s[r]:
        l += 1
        r -= 1
    else:
        print("Not palindrome")
        break
else:
    print("Palindrome")        