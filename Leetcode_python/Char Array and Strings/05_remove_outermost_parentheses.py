# Link:-https://leetcode.com/problems/remove-outermost-parentheses/description/
# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        res = ""
        i = 0
        n = len(s)
        while i < len(s):
            if s[i] == "("  and count == 0:
                count+=1
            elif s[i] == "(" and count >= 1:
                count += 1
                res += s[i]
            elif s[i] == ")" and count > 1:
                count -= 1
                res += s[i]
            elif s[i] == ")" and count == 1:
                count -= 1
            i += 1
        return res