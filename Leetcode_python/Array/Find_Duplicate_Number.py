# link :- https://leetcode.com/problems/find-the-duplicate-number/description/
# Input: nums = [1,3,4,2,2]
# Output: 2

class Solution:
    def findDuplicate(self, nums):
        #linked list cyclic problem technique
        # slow will run one step and fast will jump from elemnt->element
        # if fast == slow, means duplicate otherwise out of loop
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        
        #if fast == slow, then put fast on nums[0]
        #iterate for slow and fast on one step run , where fast == slow that is duplicate
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

input = [1,3,4,2,2]
print(Solution.findDuplicate(input))