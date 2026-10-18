# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        head = l1
        while l1 or l2:
            if l1 == None:
                curr = l2.val
            elif l2 == None:
                curr = l1.val
            else:
                curr = l1.val + l2.val
            curr += carry
            carry = 0
            if curr >= 10:
                curr -= 10
                carry = 1
            tail.next = ListNode(curr)
            tail = tail.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry != 0:
            tail.next = ListNode(carry)
        return dummy.next

            
