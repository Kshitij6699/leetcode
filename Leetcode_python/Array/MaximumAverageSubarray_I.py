# Link :- https://leetcode.com/problems/maximum-average-subarray-i/description/
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #need two pointer 
        left = 0
        right = k
        #two variable to store Sum
        window = 0 #for window sum
        ans = 0 #max of window sum

        #loop to calculate the first window sum
        for i in range(k):
            window += nums[i]
        ans = window / k

        #iterate for next windows from k
        for right in range(k,len(nums)):
            window += nums[right] - nums[right - k]
            ans  = max(ans, window/k)
        
        return ans

input  = [1,12,-5,-6,50,3], k = 4
print(Solution().findMaxAverage(input,k))