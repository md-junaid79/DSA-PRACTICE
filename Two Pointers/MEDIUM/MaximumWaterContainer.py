'''
Q.) You are given an array of integers where each element represents the height of a vertical bar. You may choose any two bars to form a container. The width of the container is the distance between the two bars, and its height is determined by the shorter of the two bars. 
Write a function to return the maximum amount of water that can be stored in such a container.
Example:
Input: [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
(The container formed by the bars at indices 1 and 8 stores the maximum water: width = 7, height = 7, area = 7 × 7 = 49.)
'''

def maxAmountOfWater(arr):
    left,right=0,len(arr)-1      # two pointers
    res=-1
    
    while left<right:
        water=min(arr[left],arr[right])*(right-left)     # width * height
        res=max(res,water)
        #moving the pointer
        if arr[left]<arr[right]:
            left+=1
        else:
            right-=1
    return res



arr=[4,3,2,1,4]
print(maxAmountOfWater(arr))  # Output: 16
        
    
    