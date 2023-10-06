# Link:- https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
# If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).

import math
class Solution:
    def isPossibleSolution(self,nums,k,mid):
        n =len(nums)
        sum = 0
        for i in range(n):
            sum += math.ceil(nums[i]/mid)
        if sum <= k:
            return True
        else:
            return False

    def smallestDivisor(self, nums, threshold):
        n =len(nums)
        start = 1
        end = max(nums)
        while(start <= end):
            mid = int(start + (end - start)/2)
            if(Solution().isPossibleSolution(nums,threshold,mid)):
                end = mid - 1
            else:
                start = mid + 1
        return start
    
nums = [1,2,5,9]
threshold = 6
print(Solution().smallestDivisor(nums,threshold))