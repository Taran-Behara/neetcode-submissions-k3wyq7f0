"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldCpy = {}
        curr = head
        count = 0
        retHead = None
        while curr:
            oldCpy[curr] = Node(curr.val)
            if count == 0:
                retHead = oldCpy[curr]
            curr = curr.next
            count = count + 1
        
        for k in oldCpy:
            if k.random and k.next:
                oldCpy[k].random = oldCpy[k.random]
                oldCpy[k].next = oldCpy[k.next]
            elif k.next:
                oldCpy[k].next = oldCpy[k.next]
            elif k.random:
                oldCpy[k].random = oldCpy[k.random]
        return retHead