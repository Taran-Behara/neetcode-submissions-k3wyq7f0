# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)
        nextLevel = []
        if root.left:
            nextLevel.append(root.left)
        if root.right:
            nextLevel.append(root.right)
        
        while len(q) > 0:
            toAdd = []
            while len(q) > 0:
                toAdd.append(q[0].val)
                q.popleft()
            res.append(toAdd)
            newNL = []
            for num in nextLevel:
                q.append(num)
                if num.left:
                    newNL.append(num.left)
                if num.right:
                    newNL.append(num.right)
            nextLevel = newNL
            for num in nextLevel:
                print(num.val)
        return res