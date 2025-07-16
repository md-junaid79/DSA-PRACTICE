'''Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive).
If the character ch does not exist in Word, do nothing.
For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). 
The resulting string will be "dcbaefd". Return the resulting string.'''

# Method-1 -> Using Two Pointers
def reversePrefix(word, ch):
    i = word.find(ch)
    if i == -1:
        return word  # ch not found, return as is

    word = list(word)  # convert to list for in-place operations
    left, right = 0, i

    while left < right:
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1

    return ''.join(word)         #converts list back to string using join by ''.join()

        
# # Method-2 -> Using String Slicing
# def reversePrefix(word, ch):
#     if ch not in word:
#         return word
#     for i in range(len(word)):
#         if word[i]==ch:
#             return word[i::-1]+word[i+1:]


print(reversePrefix("abcdefd", "d"))   # Output: "dcbaefd"
print(reversePrefix("xyxz", "z"))      # Output: "zyxx"