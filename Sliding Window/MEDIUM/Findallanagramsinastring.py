'''Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1: Input: s = "cbaebabacd", p = "abc" Output: [0,6]
Explanation: The substring with start index = 0 is "cba", which is an anagram of "abc". The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2: Input: s = "abab", p = "ab" Output: [0,1,2]
'''
from collections import Counter               #if counter is not allowed then we can use freq arr (dictionary) and ord(i) etc..
def findAnagrams (s,p): 
    len_s,len_p=len(s),len(p)
    res=[]
    if len_s<len_p:
        return res
    p_count=Counter(p)  # Count of characters in p .it returns a dictionary
    window_count=Counter(s[:len_p])  # Count of characters in the first window
    
    if window_count == p_count:
        res.append(0)

        for i in range(len_p,len_s):     #len_p to len_s because we increment right pointer 
        window_count[s[i]] += 1  # Add the new character to the window
        # left pointer is at i - len_p, removing it
        window_count[s[i - len_p]] -= 1  # Remove the character going out 
        
        if window_count[s[i-len_p]] == 0:
            del window_count[s[i - len_p]]  #deleting so that next step-> is not affected
        if window_count == p_count:
            res.append(i-len_p + 1)  
    return res
      