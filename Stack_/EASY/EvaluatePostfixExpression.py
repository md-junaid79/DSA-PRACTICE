'''Implement a function evaluatePostfix(expression) that evaluates a postfix expression and returns the result.

You will need to implement your own stack with below functions
push(): Adds item to the top of the Stack.
pop(): Removes and Returns the top item of the Stack.
peek(): Returns the top item of the Stack.
isEmpty(): Returns True if Stack is empty, False otherwise.
clear(): Removes all the items from the Stack.
size(): Returns the length of the stack.
'''

class Stack:
    def __init__(self):
        self.items=[]
    def push(self,val):
        self.items.append(val)
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    def isEmpty(self):
        return len(self.items)==0
    def clear(self):
        self.items=[]
    def size(self):
        return len(self.items)

def evaluatePostfix(expression):
    exp=expression.split()
    stack=Stack()
    
    for i in exp:
        if i.isdigit():
            stack.push(int(i))
        else:
            a=stack.pop()
            b=stack.pop()
            if i=='+':
                stack.push(b+a)
            elif i=='-':
                stack.push(b-a)
            elif i=='*':
                stack.push(b*a)
            elif i=='/':
                stack.push(b//a)
    return stack.pop()
    
        
# Example usage
print(evaluatePostfix("2 3 +"))  # Output: 5

print(evaluatePostfix("10 2 /")) # Output: 5
print(evaluatePostfix("2 10 /")) # Output: 0

print(evaluatePostfix("5 1 2 + 4 * + 3 -"))  # Output: 14