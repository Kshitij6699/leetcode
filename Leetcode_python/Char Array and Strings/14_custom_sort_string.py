# Link :- https://leetcode.com/problems/custom-sort-string/description/
# Input: order = "cba", s = "abcd"
# Output: "cbad"
# Explanation: 
# "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
# Since "d" does not appear in order, it can be at any position in the returned string. 
# "dcba", "cdba", "cbda" are also valid outputs.

from collections import Counter
class Solution:
    def customSortString(self, order, s):
        str = ''
        s1 = Counter(s)
        s2 = Counter(order)
        for i in s2:
            if i in s1:
                str += i * s1[i] #s[i] is the number of times i appears in s1,.ie how many time 'a' appeared in s
        for i in s:
            if i not in s2:
                str += i
        return str
    
        # one more way => without using Counter
        str = ''
        for i in order:
            count = s.count(i)
            if i in s:
                str += i * count
        for i in s:
            if i not in order:
                str += i
        return str