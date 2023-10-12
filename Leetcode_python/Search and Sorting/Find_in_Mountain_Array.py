# Link:- https://leetcode.com/problems/find-in-mountain-array/description/?envType=daily-question&envId=2023-10-12
# Input: array = [1,2,3,4,5,3,1], target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.


# Method:- BinarySearch
# 1. find peakelements
# 2. Seach from 0 to peak.
# 3. If not found, search from peak + 1 to 0, so this a CATCH from peak + 1 to 0 are increaing element
#    so pass boolean arguement in binary function and search opposite to normal BS fucntion.


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def peakElement(self,mountain_arr):
        start = 0
        end = mountain_arr.length() - 1
        while(start < end):
            mid  =  int(start + (end - start)/2)
            if mountain_arr.get(mid) <mountain_arr.get(mid + 1):
                start = mid + 1
            else:
                end = mid
        return end
    def binarySearch(self,mountain_arr,start,end, target, is_increasing):
        while(start <= end):
            mid =  int(start + (end - start)/2)
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) < target:
                if is_increasing == True:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if is_increasing == True:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1
    def findInMountainArray(self, target, mountain_arr):
        peak = Solution().peakElement(mountain_arr)
        ans = Solution().binarySearch(mountain_arr,0,peak,target,True)
        if ans == -1:
            ans = Solution().binarySearch(mountain_arr,peak+1,mountain_arr.length() - 1,target,False)
        return ans        