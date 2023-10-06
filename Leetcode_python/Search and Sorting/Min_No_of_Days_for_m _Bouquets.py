# Link:- https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/
# Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
# Output: 3

# Search Space Type-bipolar=> at end , start > end so return start

# We have give BloomDay with n element such that i flower will bloom on n[i] day 
# and we have to make m bouquets with k ADJACENT flowers.

# check if the mid is greater than n[i], if so count++ if not divide the count with k
# and count = 0, this will give the possible solution and if solution is possible 
# then the index will lie on left side if not then start = mid + 1.
# As this is bipolar, the answer will be start index, so return start.

class Solution:
    def isPossibleSolution(self, bloomDay, m, k , mid):
        n = len(bloomDay)
        count = 0
        res = 0
        for i in range(n):
            if bloomDay[i] <= mid:
                count += 1
            else:
                res += int(count/k)
                count = 0
        res += int(count/k)
        if res >= m:
            return True
        return False

    def minDays(self,bloomDay,m,k):
        n = len(bloomDay)
        val = m*k
        ans = 0
        if val > n:
            return -1
        start = min(bloomDay)
        end = max(bloomDay)
        while(start<=end):
            mid = int(start + (end-start)/2)
            if Solution().isPossibleSolution(bloomDay, m , k ,mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return start