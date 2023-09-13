#link :- https://leetcode.com/problems/missing-number/description/
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totalsum = n*((n+1)/2)
        sum = 0
        for i in range(n):
            sum += nums[i]
        return int(totalsum)-(sum)

input = [9,6,4,2,3,5,7,0,1]
print(Solution().missingNumber(input))