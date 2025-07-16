'''You are given an array of integers, and a target value. Your task is to find the closest sum that can be obtained by adding two numbers from the array. Return the closest sum.
Example :
Input: nums = [1, 2, 4, 7, 10], target = 12
Output: 11'''

def closestSumToTarget(nums, target):
    nums.sort()
    left,right=0,len(nums)-1
    closest_sum=float('inf')            #infnity because we want to find the minimum difference
    
    while left<right:
        curr_sum = nums[left] + nums[right]
        # Update if this sum is closer to the target
        if abs(curr_sum - target) < abs(closest_sum - target):
            closest_sum = curr_sum
        
        if curr_sum<target:
            left+=1
        elif curr_sum>target:
            right-=1
        else:
            return curr_sum
    return closest_sum
    
    
print(closestSumToTarget(nums=[-1, 5, 3, 2, 8],target=6))   