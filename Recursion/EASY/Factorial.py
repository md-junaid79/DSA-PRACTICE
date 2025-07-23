''''
Write a program to calculate factorial using recursion.
Example :
Input: n = 5
Output: 120
'''

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(4))
print(factorial(5))