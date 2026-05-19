# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = []

        stack.append((1, root))
        maxi = 0
        while stack:
            node = stack[len(stack) - 1][1]
            depth = stack[len(stack) - 1][0]
            stack.pop()
            if node and node.left:
                stack.append((1 + depth, node.left))
            if node and node.right:
                stack.append((1 + depth, node.right))
            maxi = max(maxi, depth)
        
        return maxi