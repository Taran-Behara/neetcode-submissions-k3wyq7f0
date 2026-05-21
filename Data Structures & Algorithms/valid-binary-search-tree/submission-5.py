# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, low, hi):
            if not root:
                return True
            
            if root.val >= hi or root.val <= low:
                return False
            
            return dfs(root.left, low, min(hi, root.val)) and dfs(root.right, max(low, root.val), hi)
        
        return dfs(root, float("-infinity"), float("infinity"))