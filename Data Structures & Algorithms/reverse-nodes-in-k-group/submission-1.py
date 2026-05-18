# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        point = head
        count = 0
        while point:
            count += 1
            point = point.next
        
        if count < k:
            return head
        curr = head
        prev = None
        
        count = 0
        while curr and count < k:
            currNext = curr.next
            curr.next = prev
            prev = curr
            curr = currNext
            count += 1
        
        head.next = self.reverseKGroup(curr, k)
        
        return prev