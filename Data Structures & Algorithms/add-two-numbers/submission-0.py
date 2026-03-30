# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        sec = l2

        curr = None
        carry = 0
        head = None
        while first and sec:
            nSum = carry + first.val + sec.val
            if curr:
                curr.next = ListNode(nSum % 10)
                curr = curr.next
            else:
                curr = ListNode(nSum % 10)
                head = curr
            carry = nSum // 10
            first = first.next
            sec = sec.next
        
        if first and not sec:
            while first:
                nSum = carry + first.val
                curr.next = ListNode(nSum % 10)
                curr = curr.next
                carry = nSum // 10
                first = first.next
        elif sec and not first:
            while sec:
                nSum = carry + sec.val
                curr.next = ListNode(nSum % 10)
                curr = curr.next
                carry = nSum // 10
                sec = sec.next
        
        if carry > 0:
            curr.next = ListNode(carry)
        return head