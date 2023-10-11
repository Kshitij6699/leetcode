# Link:-https://leetcode.com/problems/palindromic-substrings/
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

class Solution:
    def expand(self, s, i,j):
        count = 0
        while(i >= 0 and j<len(s) and s[i] == s[j]):
            count+=1
            i-=1
            j+=1
        return count
    def countSubstrings(self, s: str) -> int:
        countE = 0
        countO = 0
        count = 0
        for i in range(len(s)):
            # Even
            countE = Solution().expand(s,i,i+1)

            # Odd
            countO = Solution().expand(s,i,i)

            #Total count from a word for both even and odd substring
            count += countO + countE
        return count