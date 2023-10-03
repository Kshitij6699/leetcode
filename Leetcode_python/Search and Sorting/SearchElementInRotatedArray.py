# Link:- https://leetcode.com/problems/search-in-rotated-sorted-array/
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

class Solution:
    def pivotIndex(self,nums):
        s = 0
        e = len(nums) - 1

        while(s <= e):
            if(s == e):
                return s
            mid = int(s + (e-s)/2)
            if(mid -1 >= 0 and nums[mid] < nums[mid-1]):
                return mid -1
            elif(mid + 1 < len(nums) and nums[mid] > nums[mid+1]):
                return mid
            elif(nums[s] > nums[mid]):
                e = mid - 1
            else:
                s = mid + 1
        return -1

    def binarySearch(self,nums,target,s,e):
        mid = int(s + (e-s)/2)
        while(s<=e):
            mid = int(s + (e-s)/2)
            if(nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                e = mid - 1 
            else:
                s = mid + 1
        return - 1

    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1
        ans = -1
        pivot = Solution().pivotIndex(nums)

        if(nums[0] <= target and nums[pivot] >= target):
            ans = Solution().binarySearch(nums,target,0,pivot)
        else:
            ans = Solution().binarySearch(nums,target,pivot + 1, e)       
        return ans