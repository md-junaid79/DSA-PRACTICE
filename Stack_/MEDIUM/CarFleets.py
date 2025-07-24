'''There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
You are given:

An integer target representing the destination mile.
Two arrays, position and speed, both of length n:
position[i] is the starting mile of the i-th car.
speed[i] is the speed of the i-th car in miles per hour.
A car cannot pass another car but can catch up and travel next to it at the slower car's speed, forming a "fleet".

Return the number of car fleets that will arrive at the destination.
'''

def carFleet (target,position,speed):   #Don't change the number of parameters
    cars=sorted(zip(position,speed),reverse=True)
    stack=[]
    
    for pos,spd in cars:
        time=(target-pos)/spd
        
        if not stack or time>stack[-1]:  #if stack is empty or current car takes more time than last car in stack
            stack.append(time)  #add the time to stack as a new fleet
    return len(stack)  


    
print(carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))  # Output: 3
