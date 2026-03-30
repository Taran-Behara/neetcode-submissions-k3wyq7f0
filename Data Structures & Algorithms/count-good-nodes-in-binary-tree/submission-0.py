# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def getNum(self, root: TreeNode, currMax: int) -> int:
            if not root:
                return 0
            newMax = currMax
            if root.val >= currMax:
                newMax = root.val
                return getNum(self, root.left, newMax) + getNum(self, root.right, newMax) + 1
            return getNum(self, root.left, newMax) + getNum(self, root.right, newMax)
        return getNum(self, root, root.val)