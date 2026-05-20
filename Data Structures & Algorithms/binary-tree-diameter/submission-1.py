# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(root):
            if not root:
                return 0
            
            return max(1 + maxDepth(root.right), 1 + maxDepth(root.left))
        
        if not root:
            return 0
        
        return max(maxDepth(root.right) + maxDepth(root.left), self.diameterOfBinaryTree(root.right), self.diameterOfBinaryTree(root.left))