'''Given two arrays, find the intersection of the arrays, and return a result with duplicate values included. Each element in the result should appear as many times as it shows in both arrays.
Example :
Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
Output: [4, 9]
Explanation: The intersection between nums1 and nums2 is [4, 9]. The result can be in any order.
'''

#Method-1 -> Using Two Pointers after sorting both arrays
def intersectionwithDuplicates(nums1,nums2):
    nums1.sort()
    nums2.sort()
    result=[]
    
    one,two=0,0        #initializing 2 pointers for both arrays
    
    while one<len(nums1) and two<len(nums2):
        if nums1[one]==nums2[two]:
            result.append(nums1[one])
            one+=1
            two+=1
        elif nums1[one]<nums2[two]:
            one+=1
        else:
            two+=1
    return result


# #Method-2
# def intersectionwithDuplicates(nums1,nums2):
    
#     result=[]
#     for i in nums1:
#         if i in nums2:
#             result.append(i)
#             nums2.remove(i)  #to avoid counting duplicates in nums2
#     return result



print(intersectionwithDuplicates(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))  # Output: [4, 9]
print(intersectionwithDuplicates(nums1=[1, 2, 2, 1], nums2=[2, 2]))  # Output: [2, 2]