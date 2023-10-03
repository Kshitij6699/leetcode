# link:- https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# Input: nums = [3,4,5,1,2]
# Output: 1


#Method - I : element will always lie on right side of array so BS on right side
class Solution:
    def findMin(nums):
        n = len(nums)
        start = 0
        end = n - 1
        res = nums[0]
        while(start <= end):
            mid = int(start + (end - start)/2)
            if nums[mid] <= nums[end]:
                res = min(nums[mid],res)
                end = mid - 1
            else:
                start = mid + 1
        return res
    

#Method - II : Every element next to pivot Index is minimum i.e., return pivotIndex + 1