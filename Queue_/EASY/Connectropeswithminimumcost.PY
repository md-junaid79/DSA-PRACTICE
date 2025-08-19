'''You will be given array which represents length of ropes. You need to connect all the ropes with minimum cost. Cost of connecting the ropes is sum of their lengths
Input arr[] = [5,4,3,8]
Output = 39
Step 1: 4+3, the cost is 7. array will be [5,7,8]
Step 2: 5+7, the cost is 12. array will be [12,8]
Step 3: cost is 20.
Total cost is 7+ 12+ 20 = 39.
'''
    # APPROACH : put all ropes in deque.sort them and pop 1st two elements to minimize cost, add them and append to deque again. repeat until only one element in deque.

def CalculateCost(ropes):
    from collections import deque
    q=deque(ropes)
    total_cost=0
    
    while len(q)!=1:
        q=deque(sorted(q))          #deque doesn't have q.sort()
        #extract 1st & 2nd
        first=q.popleft()
        second=q.popleft()
        #get cost and append to deque
        cost=first+second
        q.append(cost)
        #add cost to total cost
        total_cost+=cost
        
    return total_cost
    
    
    
# Example usage:
print(CalculateCost([5,4,3,8]))   #Output: 39