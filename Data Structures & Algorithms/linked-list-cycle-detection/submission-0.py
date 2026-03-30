# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        if not head.next:
            return False

        slow = head
        fast = head.next

        while fast and slow:
            if fast == slow:
                return True
            
            if not fast.next:
                break
            fast = fast.next.next
            slow = slow.next
        return False