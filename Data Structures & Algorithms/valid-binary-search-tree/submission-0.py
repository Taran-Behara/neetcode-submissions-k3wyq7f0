# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def isValid(self, root: Optional[TreeNode], upper: int, lower: int) -> bool:
            if not root:
                return True
            
            if root.val >= upper or root.val <= lower:
                return False
            
            return isValid(self, root.right, upper, root.val) and isValid(self, root.left, root.val, lower)
        return isValid(self, root.right, sys.maxsize, root.val) and isValid(self, root.left, root.val, -sys.maxsize - 1)