# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        one = head
        two = head
        firstPass = True

        while one and two:
            if not firstPass and one == two:
                return True
            
            firstPass = False
            
            one = one.next
            if two.next:
                two = two.next.next
            else:
                return False
        
        return False