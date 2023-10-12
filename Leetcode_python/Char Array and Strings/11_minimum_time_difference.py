# Link:- https://leetcode.com/problems/minimum-time-difference/description/
# Input: timePoints = ["23:59","00:00"]
# Output: 1
# Given a list of 24-hour clock time points in "HH:MM" format, 
# return the minimum minutes difference between any two time-points in the list.

# TC:- O(N) + O(NlogN) + O(N)
# SC:- O(1) 

class Solution:
    def findMinDifference(self, timePoints):
        for i, time in enumerate(timePoints):
            hour,min = time.split(':')
            min_post_midnight = int(hour) * 60 + int(min)
            timePoints[i] = min_post_midnight
        timePoints.sort()
#Corner case, 00:00 is equivalent to 1440 minutes, i.e 12:59 = 1439 minutes, so 00:00 will be 1440.
#So, adding 1440 in timePoints[0] to subtract it from timePoints[n - 1] after sorting.
        res = 1440 + timePoints[0] - timePoints[len(timePoints) - 1]
        for i in range(1,len(timePoints)):
            diff = timePoints[i] - timePoints[i - 1]
            if diff < res:
                res = diff
        return res