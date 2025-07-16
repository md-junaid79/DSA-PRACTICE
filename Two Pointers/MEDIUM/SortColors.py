'''Q.)Given an array with objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. Use the integers 0, 1, and 2 to represent the colors red, white, and blue, respectively. Solve this problem without using the library's sort function.
Example :
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]'''

def sortColors(arr):
    # Use three pointers: Dutch National Flag APPROACH (2-Pointer, 1-Pass)
    #     low: points to the next position for 0.
    #     mid: current index being processed.
    #     high: points to the next position for 2 (from the end).
    
    low,mid,high=0,0,len(arr)-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:  # arr[mid] == 2
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr


nums = [2, 0, 2, 1, 1, 0]
print(sortColors(nums)
)  # Output: [0, 0, 1, 1, 2, 2]
