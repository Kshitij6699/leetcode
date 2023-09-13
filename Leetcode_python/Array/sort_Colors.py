#link :- https://leetcode.com/problems/sort-colors/description/
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
class Solution():
    def sort_colors(self,nums):
        left = 0
        index = 0
        right = len(nums)-1
        while(index <= right):
            if nums[index] == 0:
                nums[index] ,nums[left] = nums[left], nums[index]
                index += 1
                left = left + 1
            elif nums[index] == 2:
                nums[index] ,nums[right] = nums[right], nums[index]
                right = right - 1
            else:
                index += 1
        return nums

input = [2,0,2,1,1,0]
print(Solution().sort_colors(input))