'''Given a binary array containing only 0s and 1s, find the maximum number of consecutive 1s that can be obtained by flipping at most K 0s.
Write a function that takes a binary array and an integer K as input and returns the maximum number of consecutive 1s.
Example.
Input: nums= [1, 0, 1, 1, 0]
 k = 1
Output:4 
'''

def maxConsecutiveOnesWithFlips(nums, k):
    left=0
    max_len=0
    for right in range(len(nums)):
        if nums[right]==0:         #if 0 then flip it
            k-=1                   #flipped it
        while k<0:                 #if flips are exhausted
            if nums[left]==0:      #if left pointer is at 0 then restore the flip
                k+=1       
            left+=1                #slide the window from left until we find a 0 to flip
        max_len=max(max_len,right-left+1)  
    return max_len      
        

'''The algorithm keeps a window [left..right] that always satisfies: number of zeros in the window ≤ original k 
(we track this by decrementing k for each zero added and incrementing when we drop a zero).
We expand right greedily and only move left when the window becomes invalid (too many zeros). 
This ensures we examine each element O(1) times → O(n) total.'''

# Example usage
nums=[1, 0, 1, 1, 0]
print(maxConsecutiveOnesWithFlips(nums, 1))  # Output: 4

nums2=[0, 0, 1, 1, 0, 1, 1, 0, 1]
print(maxConsecutiveOnesWithFlips(nums2, 2))  # Output: 5