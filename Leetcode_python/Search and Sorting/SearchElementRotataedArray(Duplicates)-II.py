# link :- https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        s = 0
        e = len(nums) - 1
        while(s <= e):
            mid = int(s + (e - s)/2)
            if nums[mid] == target:
                return True
            if nums[s] == nums[mid] and nums[mid] == nums[e]:
                s += 1
                e -= 1
                continue
            if(nums[mid] <= nums[e]):
                if(nums[mid] <= target and target <= nums[e]):
                    s = mid + 1
                else:
                    e = mid - 1
            else:
                if nums[s] <= target and nums[mid] >= target:
                    e = mid - 1
                else:
                    s = mid + 1                
        return False