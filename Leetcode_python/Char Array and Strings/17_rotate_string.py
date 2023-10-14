# Link :- https://leetcode.com/problems/rotate-string/description/
# Input: s = "abcde", goal = "cdeab"
# Output: true

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Method - I
        # return len(s) ==len(goal) and s in goal+goal

        # Method - II
        
        # return true if s==goal
        if s == goal:
            return True
        
        # keeping string letters in list
        s , goal = [*s], [*goal]

        for i in range(len(s)):
            a = s[0]
            s.pop(0)
            s.append(a)

            if s == goal:
                return True
        return False
            