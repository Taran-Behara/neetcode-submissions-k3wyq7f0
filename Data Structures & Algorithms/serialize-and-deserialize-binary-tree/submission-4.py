# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = ""
        q = collections.deque()
        
        q.appendleft(root)
        while q:
            top = q.pop()
            if top:
                res += str(top.val) + ","
                q.appendleft(top.left)
                q.appendleft(top.right)
            else:
                res += "null,"
            
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        arr = data.split(",")

        ['1', '2', '3', 'null', 'null', '4', '5', 'null', 'null', 'null', 'null', '']
        q = collections.deque()
        root = TreeNode(val = int(arr[0]), left = None, right = None)
        q.appendleft(root)
        index = 1
        while q and index < len(arr):
            top = q.pop()
            if arr[index] != "null":
                top.left = TreeNode(val = int(arr[index]), left = None, right = None)
            index += 1
            if index < len(arr) and arr[index] != "null":
                top.right = TreeNode(val = int(arr[index]), left = None, right = None)
            if top.left:
                q.appendleft(top.left)
            if top.right:
                q.appendleft(top.right)
            index += 1


        return root


    

        

        
