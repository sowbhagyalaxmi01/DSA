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