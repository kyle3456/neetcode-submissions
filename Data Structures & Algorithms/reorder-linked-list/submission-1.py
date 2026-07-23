# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        
        curr = s.next
        s.next = None
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        back = prev
        start = head

        while start:
            tmp1 = start.next
            if back is None:
                tmp2 = None
            else:
                tmp2 = back.next
            start.next = back
            if back is None:
                break
            else:           
                back.next = tmp1
            start = tmp1
            back = tmp2



            
