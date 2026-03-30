# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0], None, None)

        leftIn = inorder[:inorder.index(root.val)]
        leftPre = preorder[1:(1 + len(leftIn))]

        rightIn = inorder[(inorder.index(root.val) + 1):]
        rightPre = preorder[(1 + len(leftIn)):]

        root.left = self.buildTree(leftPre, leftIn)
        root.right = self.buildTree(rightPre, rightIn)
        return root