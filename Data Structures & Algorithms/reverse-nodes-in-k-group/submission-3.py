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
        kth = head
        tailGroup = None
        curr = head
        while True:
            kth = curr
            count = 0
            while kth and count < k - 1:
                count += 1
                kth = kth.next
            
            
            if tailGroup:
                if not kth:
                    print(tailGroup.val)
                if kth:
                    tailGroup.next = kth
                else:
                    tailGroup.next = curr
            
            if not kth:
                break
            
            kthNext = kth.next
            tailGroup = curr
            prev = None
            print("TailGroup", tailGroup.val if tailGroup else -1)
            print("Kth", kth.val if kth else -1)
            print("Prev", prev.val if prev else -1)
            print("Curr", curr.val if curr else -1)
            print("KthNext", kthNext.val if kthNext else -1)
            print()
            while curr and curr != kthNext:
                currNext = curr.next
                curr.next = prev
                prev = curr
                curr = currNext
            
            if res == head:
                res = prev
            
            curr = kthNext
        
        return res
            
            