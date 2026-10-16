# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        total = 0
        h = head
        while h:
            total += 1
            h = h.next
        
        r = total - n
        h = head
        if r == 0:
            return h.next
        for i in range(r):
            prev = h
            h = h.next

        prev.next = h.next
        return head
