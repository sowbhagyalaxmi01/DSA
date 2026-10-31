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