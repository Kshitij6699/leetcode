# link :- https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
# Input: nums = [3,1,4,1,5], k = 2
# Output: 2

class Solution:
    def binarySearch(self,nums, s,e,target):
        mid = int(s + (e-s)/2)
        while(s <= e):
            mid = int(s + (e-s)/2)
            if(nums[mid] == target):
                return mid
            elif nums[mid] > target:
                e = mid - 1
            else:
                s = mid + 1
        return -1
    def findPairs(self,nums,k):
        nums.sort()
        set1 = set()
        for i in range(len(nums)):
            if(Solution().binarySearch(nums,i+1,len(nums)-1, nums[i]+k) != -1):
                set1.add((nums[i],nums[i]+k))
        return len(set1)