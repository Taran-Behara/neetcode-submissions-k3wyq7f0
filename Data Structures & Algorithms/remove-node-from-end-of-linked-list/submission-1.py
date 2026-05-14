# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            currNext = curr.next
            curr.next = prev
            prev = curr
            curr = currNext
        
        prevNode = None
        curr = prev
        count = 1
        res = prev

        while curr:
            currNext = curr.next
            if count == n:
                if not prevNode:
                    res = currNext
                    del curr
                    break
                prevNode.next = currNext
                del curr
                break
            prevNode = curr
            curr = currNext
            count += 1
        
        curr = res
        prev = None
        while curr:
            currNext = curr.next
            curr.next = prev
            prev = curr
            curr = currNext
        
        return prev
