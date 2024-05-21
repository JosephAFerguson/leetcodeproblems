# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trav(self, root,res,st):
        #par = parent node
        #d = direction traversed in, true = left, false = right
        if not root:
            return
        
        st.append(str(root.val))

        if not root.left and not root.right:
            res.append("->".join(st))

        self.trav(root.left, res, st )
        self.trav(root.right, res, st)
        
        st.pop()


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        st = []
        res = []
        self.trav(root, res, st)
        return res
