# link :- https://leetcode.com/problems/largest-odd-number-in-string/description/
# Input: num = "35427"
# Output: "35427"
# Explanation: "35427" is already an odd number.

class Solution:
    def largestOddNumber(self, num: str) -> str:
        # if int(num) % 2 != 0:
        #     return num
        # nums = list(num)
        # ans = 0
        # for i in range(len(nums)):
        #     if int(nums[i]) % 2 != 0:
        #         ans = max(ans, int(nums[i]))
        # if ans == 0:
        #     return ''
        # else:
        #     return str(ans)

        

        for i in range(len(num) - 1, -1,-1):
            if int(num[i]) % 2 != 0:
                return num[0:i+1]
        return ''