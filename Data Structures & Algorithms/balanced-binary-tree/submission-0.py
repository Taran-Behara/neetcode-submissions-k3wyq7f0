# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isB = True
        def isB(self, root: Optional[TreeNode]) -> int:
            if not root:
                return -1
            if not root.left and not root.right:
                return 0
            
            left = isB(self, root.left)
            right = isB(self, root.right)
            if abs(left - right) > 1:
                self.isB = False
            return max(left, right) + 1
        isB(self, root)
        return self.isB