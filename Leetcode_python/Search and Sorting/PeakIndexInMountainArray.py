# link:- https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
# Input: arr = [0,2,1,0]
# Output: 1

class Solution:
    def peakIndexInMountainArray(self, arr):
        # condition 1:-
        # Before peak => A where arr[i] < arr[i+1]
        # else:- 
        # after peak  => B where arr[i] > arr[i-1]
        # at peak  => peak where arr[i-1] < peak and peak > arr[i+1]

        start = 0
        end = len(arr) - 1

        while( start < end ):
            mid = int(start + (end - start)/2)
            if arr[mid] < arr[mid + 1]:
                start = mid + 1
            else: #arr[mid] > arr[mid - 1]
                end = mid
        return end
input = [0,2,1,0]
print(SOlution().peakIndexInMountainArray(input))

        