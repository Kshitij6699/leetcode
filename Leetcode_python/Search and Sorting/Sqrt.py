# link:- https://leetcode.com/problems/sqrtx/
# Input: x = 8
# Output: 2

class Solution:
    def mySqrt(self, x: int) -> int:
        s = 0
        e = x
        mid = int(s + (e-s)/2)
        ans  = -1
        while(s<=e):
            mid = int(s + (e-s)/2)
            if(mid * mid == x):
                return mid
            elif(mid * mid < x):
                ans = mid
                s = mid + 1
            else:
                 e = mid - 1
        return ans