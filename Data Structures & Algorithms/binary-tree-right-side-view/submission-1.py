# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = collections.deque()
        q.appendleft(root)
        res = []

        while q:
            levelNodes = []
            while q:
                toAdd = q.pop()
                levelNodes.append(toAdd)
            
            res.append(levelNodes[0].val)
            for node in levelNodes:
                if node.right:
                    q.appendleft(node.right)
                
                if node.left:
                    q.appendleft(node.left)
        
        return res

            

                        