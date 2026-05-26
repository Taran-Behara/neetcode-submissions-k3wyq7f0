# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.sort = []
        def dfs(root):
            if not root.left and not root.right:
                self.sort.append(root.val)
                return
            
            if root.left:
                dfs(root.left)
            self.sort.append(root.val)
            if root.right:
                dfs(root.right)
        dfs(root)
        return self.sort[k - 1]