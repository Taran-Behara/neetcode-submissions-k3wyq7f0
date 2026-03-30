# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def getDiam(self, root: Optional[TreeNode]) -> int:
            if not root.left and not root.right:
                newRes = 0
                if newRes > self.res:
                    self.res = newRes
                return 1
            left = 0
            right = 0
            if root.left:
                left = getDiam(self, root.left)
            if root.right:
                right = getDiam(self, root.right)
            newRes = left + right
            if newRes > self.res:
                self.res = newRes
            return max(left, right) + 1
        getDiam(self, root)
        return self.res