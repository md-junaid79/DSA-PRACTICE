# Q.)Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases. A palindrome is a sequence of characters that reads the same forward as backward.

def isPalindrome(s):
    cleaned=''.join(i.lower() for i in s if i.isalnum())
    left,right=0,len(cleaned)-1     #two pointers
    while left<right:
        if cleaned[left]!=cleaned[right]:
            return False
        left+=1                 #inc left
        right-=1                #dec right
    return True




print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))                      # False
