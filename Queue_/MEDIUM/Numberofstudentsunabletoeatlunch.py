'''At a school cafeteria, students stand in a queue to get sandwiches for lunch. The cafeteria offers circular and square sandwiches, represented by numbers 0 and 1 respectively. Each student has a preference for either circular or square sandwiches.

You are given two integer arrays:
students: Represents the preferences of the students in the initial queue. The ith element of this array (0-indexed) indicates the preference of the ith student in the queue, where 0 represents a preference for circular sandwiches and 1 represents a preference for square sandwiches.

sandwiches: Represents the types of sandwiches in the cafeteria stack. The ith element of this array (0-indexed) indicates the type of the ith sandwich in the stack, where 0 represents a circular sandwich and 1 represents a square sandwich.
 
The process of serving sandwiches proceeds as follows:
If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the end of the queue.
This process continues until none of the students in the queue want to take the top sandwich and are thus unable to eat.
'''

# APPROACH : stuendts->deque .attempts,sand_idx=0,while attempts<len(q) and q: check student takes sandwich or not.if yes pop and increment sand_idx and make attempts=0.
# else: add to rear end and increment attempts.

from collections import deque
def countStudents(students,sandwiches):
    q=deque(students)
    sand_idx=0
    attempts=0
    
    while q and attempts<len(q):
        # Check if the student at the front of the queue prefers the sandwich on top of the stack
        if q[0]==sandwiches[sand_idx]:
            # If they do, they take the sandwich and leave the queue
            q.popleft()
            sand_idx+=1
            attempts=0     #resert attempts since a sandwich was taken
        else:
            q.append(q.popleft())
            attempts+=1       #attempts incereased since the student didn't take the sandwich
            
    return len(q)             #remaining students who cannot eat




# Example usage:
print(countStudents([1,1,0,0],[0,1,0,1]))  #Output: 0
print(countStudents([1,1,0,0],[1,0,0,1]))  #Output: 2
    