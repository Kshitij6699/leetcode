# Link:-https://leetcode.com/problems/reverse-linked-list/description/
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if head == None:
            return head
        if head.next == None:
            return head
        prev = None
        curr = head
        while(curr!=None):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        