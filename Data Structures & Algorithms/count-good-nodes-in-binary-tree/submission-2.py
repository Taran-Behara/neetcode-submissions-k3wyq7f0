# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, numGood, highest):
            if not root:
                return 0
            
            if root.val >= highest:
                return 1 + dfs(root.left, numGood + 1, root.val) + dfs(root.right, numGood + 1, root.val)
            
            return dfs(root.left, numGood, highest) + dfs(root.right, numGood, highest)
        
        return dfs(root, 0, float("-infinity"))
            