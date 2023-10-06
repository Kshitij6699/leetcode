# Link:- https://leetcode.com/problems/kth-missing-positive-number/description/
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. 
# The 5th missing positive integer is 9.

# Method -I:- Brute force O(n), loop through array and if the element is less than or equal to k, 
# increment k else break and return k.

# Method - II:- "Binary Search and Maths" , search for arr[mid] - (mid + 1) < k

# Maths difference
# for [2,3,4,7,11] , the missing element till 0th position will be A[0] - (0 + 1)
# Ex. 2 - (0 + 1) = 1.
# so search for that difference where k is less.
# The position on which k is less is the position where the missing element will lie on left side and that will be pointer by END pointer.
# so we can return " k + end + 1" or "k + start".

class Solution:
    def findKthPositive(self, arr, k):
        # Method - I
        # n = len(arr)
        # for i in range(n):
        #     if arr[i] <= k:
        #         k += 1
        #     else:
        #         break
        # return k

        # Method -II
        n = len(arr)
        start = 0
        end = n -1
        while(start <= end):
            mid = (start + end) // 2
            if arr[mid] - (mid + 1) < k:
                start = mid + 1
            else:
                end = mid - 1
        return k + end + 1