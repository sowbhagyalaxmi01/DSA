###container with most water----------------


hts = list(map(int,input().split()))#1 2 4 2 6 5
                                    #0 1 2 3 4 5
                                    #        L
                                    #        R
n = len(hts)#6

left = 0#0
right = n-1#5
max_area = 0#0

while left<right:#1<5

    area = min(hts[left], hts[right])*(right-left)#1*5=5, 2*3=6, 4*3=12, 2*2=4, 5*1=5

    max_area = max(area, max_area)#12

    if hts[left]<hts[right]:
        left+=1
    else:
        right-=1

print(max_area)




#Reverse String
s= list(map(int,input().split()))
left=0
right=len(s)-1
while left<right:
    s[left],s[right]=s[right],s[left]
    left+=1
    right-=1
print(s)    


#Valid Palindrome — LeetCode 125(also requires ignoring spaces, punctuation, and capitalization.)
s = "A man, a plan, a canal: Panama"

s = ''.join(ch.lower() for ch in s if ch.isalnum())

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



#Remove Duplicates from Sorted Array
nums = [1, 1, 2, 2, 3]

left = 0

for right in range(1, len(nums)):
    if nums[left] != nums[right]:
        left += 1
        nums[left] = nums[right]

print(nums[:left + 1])
print(left + 1)



#Move Zeroes
nums = [0, 1, 0, 3, 12]

left = 0

for right in range(len(nums)):
    if nums[right] != 0:
        nums[left] = nums[right]
        left += 1

while left < len(nums):
    nums[left] = 0
    left += 1

print(nums)


#Squares of a Sorted Array 
nums = [-4, -1, 0, 3, 10]

left = 0
right = len(nums) - 1
result = [0] * len(nums)

k = len(nums) - 1

while left <= right:
    if abs(nums[left]) > abs(nums[right]):
        result[k] = nums[left] ** 2
        left += 1
    else:
        result[k] = nums[right] ** 2
        right -= 1
    k -= 1

print(result)



#3Sum
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result