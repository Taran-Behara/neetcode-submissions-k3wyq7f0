# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKth(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        curr = head
        res = None
        while count < k:
            res = curr
            if res is None:
                break
            curr = curr.next
            count = count + 1
        return res
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        kth = self.getKth(head, k)
        res = kth
        kNext = kth.next
        nextKth = self.getKth(kth.next, k)
        curr = head
        prev = None
        if not kth:
            return head
        if not kNext and kth:
            while curr:
                currNext = curr.next
                curr.next = prev
                prev = curr
                curr = currNext
            return prev
        while kth:
            while curr:
                currNext = curr.next
                if not prev:
                    if not nextKth:
                        curr.next = kNext
                    else:
                        curr.next = nextKth
                else:
                    curr.next = prev
                if curr == kth:
                    break
                prev = curr
                curr = currNext
            curr = kNext
            prev = None
            kth = nextKth
            if not kth:
                break
            kNext = kth.next
            nextKth = self.getKth(kth.next, k)
        if res:
            return res
        return head