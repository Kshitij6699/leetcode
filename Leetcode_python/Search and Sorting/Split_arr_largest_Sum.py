# Link:- https://leetcode.com/problems/split-array-largest-sum/description/
# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

# Search Space, Range(max,sum)

# Method - I: Brute Force : Linear Search :- O(N*N)
# Method - II: Binary Search :- O(N*LogN)

# 1. Find Range for the Search.
# 2. Once the Range is determined , search in that search space for sum which is manimum of 
# those maximum/ possible solutions.



class Solution:
    def isPossibleSolution(self, nums, k , mid):
        n = len(nums)
        count = 1
        Tsum = 0
        for i in range(n):
            if nums[i] + Tsum > mid:
                count += 1
                Tsum = nums[i]
                if count > k:
                    return False
            else:
                Tsum += nums[i]
        return True
    def splitArray(self, nums, k):
        start = max(nums)
        end = sum(nums)
        while(start <= end):
            mid = (start + end)//2
            if Solution().isPossibleSolution(nums, k, mid):
                end = mid - 1
            else:
                start = mid + 1
        return start
