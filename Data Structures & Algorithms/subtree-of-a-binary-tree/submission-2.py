# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(one, two):
            if not one and not two:
                return True
            
            if not one or not two or one.val != two.val:
                return False
            

            left = sameTree(one.left, two.left)
            right = sameTree(one.right, two.right)
            return left and right
        
        if not root or not subRoot:
            return False
        
        if root.val == subRoot.val:
            if sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right):
                return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)