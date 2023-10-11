# Link:- https://leetcode.com/problems/valid-palindrome-ii/description/
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# can remove only element and check whether that string is palindrome 

class Solution:
    def checkPalindrome(self, s, i, j):
        while(i<=j):
            if s[i]!=s[j]:
                return False
            i += 1
            j -= 1
        return True
    def validPalindrome(self,s):
        ans = 0
        i = 0
        n = len(s)
        j = n - 1
        while(i <= j):
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                ans = Solution().checkPalindrome(s, i+1, j) 
                ans1 = Solution().checkPalindrome(s, i, j -1)
                return ans or ans1
        return True