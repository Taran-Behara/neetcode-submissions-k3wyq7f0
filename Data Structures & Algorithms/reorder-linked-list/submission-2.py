# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None
        prev = slow.next

        while curr:
            currNext = curr.next
            curr.next = prev
            prev = curr
            curr = currNext
        
        currTail = prev
        currHead = head

        while currTail:
            currHeadNext = currHead.next
            currTailNext = currTail.next
            currHead.next = currTail
            currTail.next = currHeadNext
            currHead = currHeadNext
            currTail = currTailNext