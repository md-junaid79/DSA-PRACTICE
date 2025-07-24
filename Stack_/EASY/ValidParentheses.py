'''You are given a string consisting of the characters '(', ')', '{', '}', '[', and ']'.
A string is considered valid if:

Every opening bracket has a corresponding closing bracket of the same type.
Brackets are closed in the correct order.
Every closing bracket has a preceding matching opening bracket.
Write a function to determine if the input string is valid. Return true if valid, and false otherwise.

Example:
Input: "()"
Output: true
'''


def isStringValid(s):
    openb = {'(', '[', '{'}                 #set of opening brackets
    closeb = {')': '(', ']': '[', '}': '{'} #dictionary of closing brackets
    stack = []

    for ch in s:
        if ch in openb:
            stack.append(ch)
        elif ch in closeb:
            if not stack or stack[-1] != closeb[ch]:
                return False
            stack.pop()

    return len(stack) == 0
