# Link :- https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

# Input: s = "daabcbaabcbc", part = "abc"
# Output: "dab"
# Explanation: The following operations are done:
# - s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
# - s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
# - s = "dababc", remove "abc" starting at index 3, so s = "dab".
# Now s has no occurrences of "abc".

class Solution:
    def removeOccurrences(self, s, part):
        while(1):
            i = s.find(part)
            if i == -1:
                break
            else:
                s=s[:i]+s[i+len(part):]
        return s