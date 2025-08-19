'''You are given a queue containing N integers and an integer K. Your task is to reverse the order of the first K elements while keeping the rest of the queue in the same order.
If the value of K exceeds the number of elements in the queue, return the queue as it is without making any modifications.
Example 1 :
queue :[1, 2, 3, 4, 5]
K :3
Output 1 :
[3, 2, 1, 4, 5]
'''
    #APPROACH : add k elemnts to stack and pop them to reverse , and then add remaining (l-k) elements to queue

def reverseElements(queue,k):
    
    from collections import deque          #deque is used for efficient pop and append operations from both the ends
    q=deque(queue)             #converting it to deque
    length=len(q)
    stack=[]
    if k>length or k<=0:
        return queue
    #add first k elements to stack
    for i in range(k):
        stack.append(q.popleft())
    #pop them from stack and add to queue . reversing done
    while stack:
        q.append(stack.pop())
    #adding remaining l-k elements to q
    for _ in range(length-k):
        q.append(q.popleft())
        
    return list(q)  #convert deque back to list before returning




# Example usage:
print(reverseElements([9,8,7,4,2,2,0],4))     #OP : [4, 7, 8, 9, 2, 2, 0]