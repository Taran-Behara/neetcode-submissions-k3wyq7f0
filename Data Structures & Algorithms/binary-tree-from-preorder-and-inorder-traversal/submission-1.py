# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder, inorder):
            if not preorder:
                return None
            root = TreeNode(val = preorder[0], left = None, right = None)
            result = preorder[1:len(preorder)]
            index = -1
            for i in range(0, len(inorder)):
                if inorder[i] == preorder[0]:
                    index = i
            
            inLeft = inorder[0:index]
            inRight = inorder[index + 1: len(inorder)]

            preLeft = result[0:len(inLeft)]
            preRight = result[len(inLeft):len(result)]

            root.left = build(preLeft, inLeft)
            root.right = build(preRight, inRight)
            return root
        return build(preorder, inorder)
            