# Link :-https://leetcode.com/problems/middle-of-the-linked-list/submissions/1100056981/
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head):
        if head is None:
            return head
        if head.next is None:
            return head
        fast = head
        slow = head
        while(fast!=None):
            fast = fast.next
            if fast != None:
                fast = fast.next
                slow = slow.next
        return slow