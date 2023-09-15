# link:- https://leetcode.com/problems/binary-search/
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

class Solution:
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1

        while(start<=end):
            mid = int(start + (end-start)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

input = [-1,0,3,5,9,12]
target = 9
print(Solution().search(input,target))