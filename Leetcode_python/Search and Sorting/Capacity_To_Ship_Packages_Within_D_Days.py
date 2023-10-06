# Link:- https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

#Given weight of the package and how many days to be shipped.
#Find the minimum weight to be shipped per day so that all packages to be shipped in given days.

#Method :- Search Space Problem
# -> find the range
# -> then search in that range

class Solution:
    def isPossibleSolution(self, weights,mid, days):
        Tsum = 0
        count = 1
        n = len(weights)
        for i in range(n):
            #check for large sum first
            if weights[i] + Tsum > mid:
                count += 1
                Tsum = weights[i]
            else:
                Tsum += weights[i]
        return count
    def shipWithinDays(self, weights, days):
        start = max(weights)
        end = sum(weights)
        ans = 0
        while(start <= end):
            mid  = int(start + (end - start)/2)
            noOfDays = Solution().isPossibleSolution(weights, mid, days)
            if noOfDays <= days:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans