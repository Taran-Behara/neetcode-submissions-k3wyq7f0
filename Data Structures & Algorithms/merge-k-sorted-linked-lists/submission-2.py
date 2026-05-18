# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwo(l1, l2):
            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
            
                tail = tail.next
        
            while l1:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
        
            while l2:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
        
            return dummy.next
        
        head = None
        for l in lists:
            head = mergeTwo(head, l)
        
        return head