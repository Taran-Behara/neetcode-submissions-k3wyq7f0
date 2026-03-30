# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def sortOrder(self, root: Optional[TreeNode], sortedTree: List[int]) -> None:
            if not root:
                return
            sortOrder(self, root.left, sortedTree)
            sortedTree.append(root.val)
            sortOrder(self, root.right, sortedTree)
        sortedTree = []
        sortOrder(self, root, sortedTree)
        return sortedTree[k - 1]