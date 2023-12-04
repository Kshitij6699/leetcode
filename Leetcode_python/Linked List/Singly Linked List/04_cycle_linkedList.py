# Link:- https://leetcode.com/problems/linked-list-cycle/submissions/1100625609/
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Method -I : using Map functionality
class Solution:
    def hasCycle(self, head):
        dict = {}
        temp = head
        while( temp != None):
            if temp in dict:
                return True
            else:
                dict[temp] = True
            temp = temp.next
        return False