# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head
        while f.next and f.next.next:
            f = f.next.next
            s = s.next
        
        curr = s.next
        s.next = None
        prev = None
        tmp = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        curr = prev
        q = head
        while curr:
            t = q.next
            q.next = curr
            tmp = curr.next
            curr.next = t
            curr = tmp
            q = t

        

