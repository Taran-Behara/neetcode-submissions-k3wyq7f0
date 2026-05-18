# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1:
            return head
        res = head
        curr = head
        tailGroup = None
        
        while True:
            kth = curr
            count = 0
            while kth and count < k - 1:
                count += 1
                kth = kth.next
            

            if tailGroup:
                if kth:
                    tailGroup.next = kth
                else:
                    tailGroup.next = curr
            
            if not kth:
                break
            

            prev = None
            kthNext = kth.next
            tailGroup = curr
            while curr and curr != kthNext:
                currNext = curr.next
                curr.next = prev
                prev = curr
                curr = currNext
            
            if res == head:
                res = prev
            
            curr = kthNext
        
        return res
