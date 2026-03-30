# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count = count + 1
            curr = curr.next
        
        nodeNum = count - n + 1

        count = 0
        prev = None
        curr = head
        while curr:
            count = count + 1
            if count == nodeNum:
                if prev == None:
                    retNode = curr.next
                    del curr
                    return retNode
                prev.next = curr.next
                del curr
                return head
            prev = curr
            curr = curr.next