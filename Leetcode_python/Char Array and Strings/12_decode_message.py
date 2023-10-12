# Link :- https://leetcode.com/problems/decode-the-message/description/
# Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
# Output: "this is a secret"
# Explanation: The diagram above shows the substitution table.
# It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over the lazy dog".

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {'':''}
        c = 97
        for i in range(len(key)):
            if key[i] not in d and key[i] != " ":
                d[key[i]] = chr(c)
                c += 1
        s = ''
        for i in range(len(message)):
            if message[i] == ' ':
                s += " "
            else:
                s += d[message[i]]
        return s        