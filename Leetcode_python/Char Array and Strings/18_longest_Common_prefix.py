# Link :- https://leetcode.com/problems/longest-common-prefix/description/
# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# comparing each character of string with others

class Solution:
    def longestCommonPrefix(self, strs):
        common=""
        # returning "" , if  List is not present 
        if len(strs)==0:
            return common
        
        # 0 to first_string length
        for i in range(len(strs[0])):
        
            for s in strs:
                if i==len(s) or s[i]!=strs[0][i]:
                    return common
            common+=strs[0][i]
        return common