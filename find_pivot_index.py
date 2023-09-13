#link:- https://leetcode.com/problems/find-pivot-index/description/
# Input: nums = [1,7,3,6,5,6]
# Output: 3
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = 0
        for i in range(len(nums)):
            totalSum += nums[i]
        leftSum = 0
        for i in range(len(nums)):
            if(leftSum * 2 == totalSum - nums[i]):
                return i
            leftSum += nums[i]
        return -1
    
input = [1,7,3,6,5,6]
print(Solution().pivotIndex(input))