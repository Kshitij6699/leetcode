# link:- https://leetcode.com/problems/valid-palindrome/
# Input: s = "A man, a plan, a canal: Panama"
# Output: true


class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        i = 0
        while(i < len(s)):
            # if((ord(s[i]) >= 48 and ord(s[i]) <= 57 ) or (ord(s[i]) >= 65 and ord(s[i]) <= 90 ) or (ord(s[i]) >= 97 and ord(s[i]) <= 122 )):
            if(s[i].isalnum()):
                string += s[i]
            i+=1
        i = 0
        j = len(string) - 1
        string  = string.lower()
        print(string)
        while(i<=j):
            if(string[i] != string[j]):
                return False
            i+=1
            j-=1
        return True
    
# s = "A man, a plan, a canal: Panama"
# output = Solution().isPalindrome(s)
# print(output)