# link :- https://leetcode.com/problems/koko-eating-bananas/description/
# Input: piles = [3,6,7,11], h = 8
# Output: 4

#you have to return the index i.e the number in the search space.
#the question says you need to find how much time req to eat all bananas,
# so the search space should be from 1 to the max of nums.

import math
class Solution:
    def totalHours(self,nums, h):
        totalhours = 0
        for i in range(len(nums)):
            totalhours += math.ceil(nums[i] / h)
        return totalhours
    def minEatingSpeed(self, piles, h):
        start = 1
        end = max(piles)
        res = float('inf')
        while(start <= end):
            mid = int(start + (end - start)/2)
            reqT = Solution().totalHours(piles, mid)
            if reqT <= h:
                res = min(res, reqT)
                end = mid - 1
            else:
                start = mid + 1
        return start