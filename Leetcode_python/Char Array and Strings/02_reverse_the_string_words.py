# Link:- https://leetcode.com/problems/reverse-words-in-a-string/solutions/1632928/intuitive-two-pointers-in-python-without-strip-or-split/
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# simple python solution , split and join reversely.

class Solution:
    def reverseWords(self,s):
        s = s.split()
        return " ".join(s[::-1])
            
