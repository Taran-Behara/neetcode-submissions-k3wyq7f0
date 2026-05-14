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
        curr = head
        oldToNew = {}
        while curr:
            newNode = Node(curr.val, None, None)
            oldToNew[curr] = newNode
            curr = curr.next
        
        curr = head
        while curr:
            print(curr.val)
            if curr.next:
                oldToNew[curr].next = oldToNew[curr.next]
            if curr.random:
                oldToNew[curr].random = oldToNew[curr.random]
            curr = curr.next
        

        if head:
            return oldToNew[head]
        return head