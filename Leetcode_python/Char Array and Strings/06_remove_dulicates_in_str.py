# link:- https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
# Input: s = "abbaca"
# Output: "ca"

# New String approach

# Method I
def removeDuplicates(s):
    string = ""
    i = 0
    while(i < len(s)):
        if (string[-1:] != s[i]):
            string += s[i]
        else:
            string = string[:-1]
        i+=1
    return string

# Method II
def removeDuplicates(s):
        index = 0
        while index + 1 < len(s):
            if s[index] == s[index+1]:
                s = s[:index] + s[index+2:]
                if index > 0:
                    index -= 1
            else:
                index += 1
        return s