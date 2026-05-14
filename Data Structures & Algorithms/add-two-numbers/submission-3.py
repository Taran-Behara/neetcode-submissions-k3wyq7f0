# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        one = l1
        two = l2

        carry = 0
        prevNode = None
        res = None
        while one and two:
            total = one.val + two.val + carry
            val = total % 10
            carry = total // 10
            if not prevNode:
                res = ListNode(val, None)
                prevNode = res
            else:
                currNode = ListNode(val, None)
                prevNode.next = currNode
                prevNode = currNode
            
            
            one = one.next
            two = two.next
        
        while one:
            total = one.val + carry
            val = total % 10
            carry = total // 10
            currNode = ListNode(val, None)
            prevNode.next = currNode
            prevNode = currNode
            one = one.next
        
        while two:
            total = two.val + carry
            val = total % 10
            carry = total // 10
            currNode = ListNode(val, None)
            prevNode.next = currNode
            prevNode = currNode
            two = two.next
        
        if carry > 0:
            prevNode.next = ListNode(carry, None)


        
        return res