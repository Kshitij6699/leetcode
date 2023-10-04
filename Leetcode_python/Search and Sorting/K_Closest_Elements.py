# link:- https://leetcode.com/problems/find-k-closest-elements/description/
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]


# use two pointer approach 
#Method I:- two Pointer with low = 0 and high = n -1 and one who has difference more will go in
#Method II:- two pointer with high will point on x and low = high - 1 and one with difference less will go out , CHECK CORNER CASES
class Solution:
    # def bs(self,arr,x):
    #     start = 0
    #     end = len(arr) - 1
    #     ans = end
    #     while (start <= end):
    #         mid = int(start + (end-start)/2)
    #         if(arr[mid] >= x):
    #             ans = mid
    #             end = mid - 1
    #         elif arr[mid] > x:
    #             end = mid - 1
    #         else:
    #             start = mid + 1
    #     return ans
    # def bs_ptr(self,arr,k,x):
    #     high = Solution().bs(arr,x)
    #     low = high - 1
    #     while(k!=0):
    #         if(low < 0):
    #             high += 1
    #         elif( high >= len(arr)):
    #             low -= 1
    #         elif(x - arr[low] < arr[high] - x):
    #             low -= 1
    #         else:
    #             high += 1
    #         k -= 1
    #     return arr[low+1:high]
    def two_ptr(self,arr,k,x):
        low = 0
        high = len(arr) - 1
        while(high - low >= k):
            if(abs(x - arr[low]) > abs(arr[high] - x )):
                low += 1
            else:
                high -= 1
        return arr[low:high+1]
    def findClosestElements(self, arr, k, x):
        return Solution().two_ptr(arr,k,x)
        # return Solution().bs_ptr(arr,k,x)
        