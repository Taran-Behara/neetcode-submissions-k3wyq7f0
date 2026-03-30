# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        def invert(self, root: Optional[TreeNode]) -> None:
            if not root.right and not root.left:
                return
            
            if not root.right and root.left:
                root.right = root.left
                root.left = None
                invert(self, root.right)
            elif root.right and not root.left:
                root.left = root.right
                root.right = None
                invert(self, root.left)
            else:
                temp = root.left
                root.left = root.right
                root.right = temp
                invert(self, root.left)
                invert(self, root.right)
        invert(self, root)
        return root