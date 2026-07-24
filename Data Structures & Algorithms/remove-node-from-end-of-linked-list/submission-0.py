# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        t = 0
        while cur:
            t += 1
            cur = cur.next
        
        #t = 4
        r = t - n
        cur = head
        prev = None
        for _ in range(r):
            prev = cur
            cur = cur.next

        if prev == None:
            head = cur.next
        else:
            prev.next = cur.next
            cur.next = None

        return head