# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        curr = head
        while curr:
            count = count + 1
            curr = curr.next
        
        ind = (count) // 2
        count = 0

        revNode = head
        while count < ind:
            count = count + 1
            revNode = revNode.next
        
        currNode = revNode
        prev = None

        while currNode:
            currNext = currNode.next
            currNode.next = prev
            prev = currNode
            currNode = currNext
        
        currNode = head
        tail = prev

        while tail.next:
            currNext = currNode.next
            nextTail = tail.next
            currNode.next = tail
            tail.next = currNext
            currNode = currNext
            tail = nextTail