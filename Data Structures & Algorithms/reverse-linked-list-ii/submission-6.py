# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        prev = None
        for i in range(1, left):
            prev = curr
            curr = curr.next
        l = curr
        l_p = prev
        prev = curr
        curr = curr.next
        for i in range(right - left):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        if l_p:
            if curr:
                l.next = curr
            else:
                l.next = None
            l_p.next = prev
            return head
        else:
            l.next = curr
        
        return prev