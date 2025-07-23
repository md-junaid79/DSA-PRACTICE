# 'Write a program to reverse String.'

def reverseString(s):
    if len(s)<=1:
        return s
    else:
        return s[-1]+reverseString(s[:-1])
    
    
print(reverseString("hello"))