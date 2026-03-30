# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxD(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            maxLeft = 1 + maxD(self, root.left)
            maxRight = 1 + maxD(self, root.right)

            return max(maxLeft, maxRight)
        return maxD(self, root)