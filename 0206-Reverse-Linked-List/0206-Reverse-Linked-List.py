# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        fwd = head       # pointer to store next node
        curr = head      # current node
        prev = None      # previous node (reversed part)

        while fwd:
            fwd = fwd.next       # store next node
            curr.next = prev     # reverse the link
            prev = curr          # move prev forward
            curr = fwd           # move curr forward
        
        return prev              # new head of reversed list