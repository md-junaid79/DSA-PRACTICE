'''Q).You are given an array of integers ‘nums’ and an integer ‘target’. Your task is to design a function, that returns the indices of two numbers in the array such that their sum equals the ‘target’.
Example :
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]'''


def TwoSumTarget(nums,target):
    
    ## Method-1 -> BRUTE FORCE
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         if nums[i]+nums[j]==target:
    #             return [i,j]
    # return []  # No solution found\
    
    #Method-2 -> Two Sum Using Hash Map 
    seen_dict={}
    for index,num in enumerate(nums):
        #using a hash map to store the COMPLEMENT
        compli=target-num
        if compli in seen_dict:                       # if complement in dict.keys() then return their values(indices)
            return sorted([index,seen_dict[compli]])  #returning num indexx and complement index in sorted order
        seen_dict[num]=index                          # storing the number and its index in the dict
                        
        
    ## Method-3 -> Two Sum Using Two Pointers by sorting 
    # left,right=0,len(nums)-1  # two pointers
    # nums.sort()              # sorting changes the indices so it may fail  test cases so dont prefer this approach if indices matter
    # while left<right:
    #     curr_sum=nums[left]+nums[right]
    #     if curr_sum==target:
    #         return [left, right]
    #     elif curr_sum<target:
    #         left+=1
    #     else:
    #         right-=1
    # return []  # No solution found


print(TwoSumTarget(nums=[2, 7, 11, 15],target=9))

print(TwoSumTarget(nums=[-1, -2, -3, -4, -5],target=-8))
