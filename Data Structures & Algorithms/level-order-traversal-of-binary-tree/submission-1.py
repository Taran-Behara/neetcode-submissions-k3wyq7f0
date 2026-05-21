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
        q = collections.deque()
        q.appendleft(root)
        res = []
        while q:
            levelNodes = []
            level = []
            while q:
                toAdd = q.pop()
                levelNodes.append(toAdd)
                level.append(toAdd.val)
            
            res.append(level)
            for node in levelNodes:
                if node.left:
                    q.appendleft(node.left)
                
                if node.right:
                    q.appendleft(node.right)
            
        
        return res