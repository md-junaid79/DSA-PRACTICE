'''You are tasked with implementing the next permutation function. This function rearranges numbers in an array to the lexicographically next greater permutation. If such an arrangement is not possible, it must rearrange the array to the lowest possible order (sorted in ascending order). Modify the given array in place and return the newly arranged array.
Example :
Input: [1, 2, 3]
Output: [1, 3, 2]
'''

def nextPermutation(arr):
    n=len(arr)
    pivot=-1
    #find a pivot element where its less than the next element ex: 1 , 7
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            pivot=i
            break               
    # not pivot then reverse
    if pivot==-1:
        return list(reversed(arr))           #as reversed returns an iterator, not a list
    #find greater elemnet from right than pivot and swap it
    for i in range(n-1,-1,-1):
        if arr[i]>arr[pivot]:
            arr[i],arr[pivot]=arr[pivot],arr[i]
            break
    #reverse the elements after pivot
    return arr[:pivot+1]+(arr[:pivot:-1])    #-1 indicates backward slicing



print(nextPermutation(arr=[2,4,1,7,5,0]))
print(nextPermutation(arr=[3,2,1]))

    
    
    
    