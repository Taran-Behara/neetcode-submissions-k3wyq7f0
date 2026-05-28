# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = ""
        def preorder(root):
            if not root:
                return
            self.res += str(root.val)
            self.res += " "
            preorder(root.left)
            preorder(root.right)
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.res += str(root.val)
            self.res += " "
            inorder(root.right)
        
        preorder(root)
        inorder(root)
        return self.res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        nums = data.split(" ")
        nums.pop()
        for i in range(0, len(nums)):
            nums[i] = int(nums[i])
        preorder = nums[0:len(nums)//2]
        inorder = nums[len(nums)//2:len(nums)]
        
        def build(preorder, inorder):
            if not preorder or not inorder:
                return None
            
            root = TreeNode(val = preorder[0], left = None, right = None)

            index = -1
            for i in range(0, len(inorder)):
                if inorder[i] == preorder[0]:
                    index = i
            result = preorder[1:]

            inLeft = inorder[0:index]
            inRight = inorder[index + 1:len(inorder)]

            preLeft = result[0:len(inLeft)]
            preRight = result[len(inLeft):len(result)]

            root.left = build(preLeft, inLeft)
            root.right = build(preRight, inRight)
            return root
        return build(preorder, inorder)
