'''You are given N bags, each containing some number of diamonds. You can perform exactly K operations, where in each operation:

Select the bag with the maximum number of diamonds.
Collect all diamonds from it.
Put back half of the collected diamonds (integer division by 2).
Your task is to determine the maximum number of diamonds that can be collected after performing K operations.

For example, if N = 4, arr = [5, 3, 8, 6], and K = 3, the maximum diamonds that can be collected is 19.
'''
#APPROACH : Sort queue each time (deque(sorted(q)))-> select max bag-> add to total diamonds->put back half ->repeat until k time for i in range(k) OR wihle k!=0 

from collections import deque
def findmaximumDiamonds(N,arr,k):
    diamonds=0
    q=deque(arr)

    while k!=0:
        q=deque(sorted(q))  
        #Select the bag with the maximum number of diamonds.
        max_bag=q.pop()
        #Collect all diamonds from it.
        diamonds+=max_bag
        #Put back half of the collected diamonds (integer division by 2).
        q.append(max_bag//2)
        
        k-=1
    return diamonds
        
        
        
        
        
        
        
        
        
#DRAWBACKS :
'''Each iteration you do q = deque(sorted(q)) → sorting costs O(N log N).
You repeat this for k steps.
So total time complexity = O(k · N log N).'''

# ✅ Optimized way (using heap)
'''Normally, we’d use a max heap (priority queue):
Extract max in O(log N)
Insert half back in O(log N)
Total complexity = O(k log N) (much faster than re-sorting each time)'''