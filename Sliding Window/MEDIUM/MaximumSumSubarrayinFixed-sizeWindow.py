'''You are given an array of integers and a fixed window size. Your task is to find the maximum sum subarray within the given window size. The window slides through the array, and at each step, you need to compute the sum of elements within the current window.
Example.
Input:
nums = [2, 1, 5, 1, 3, 2]
k = 3;
Output:9
'''

def maxSumSubarray(nums, k):
    if not nums or k>len(nums):          #if k is more then no subarray can be formed
        return 0
    left,right=0,k-1                     #initiate L&R pointers
    max_sum=float('-inf')
    
    while right<len(nums):                
        curr_sum=0                       # to track current sum                
        for i in range(left,right+1):    #sum of elements in the current window . alternate way is to use : sum(nums[left:right+1])
            curr_sum+=nums[i]
        max_sum=max(max_sum,curr_sum)    #update max_sum if current sum is greater
        #slide the window
        left+=1
        right+=1
    return max_sum
        
        
        
# Example usage
print(maxSumSubarray([2, 1, 5, 1, 3, 2], 3))  # Output: 9
print(maxSumSubarray([1, 2, 3, 4, 5], 2))  # Output: 9