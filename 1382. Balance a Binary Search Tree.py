# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        tre = []
        def InOrd(root,curr):
            if not root:
                return
            InOrd(root.left,curr)
            curr.append(root.val)
            InOrd(root.right,curr)

        InOrd(root,tre)
        l , r = 0 ,len(tre)-1
        def make(l, r, vals):
            if l >r:
                return None
            m = (l+r)//2
            root = TreeNode(vals[m])
            root.left = make(l, m-1,vals)
            root.right = make( m+1,r,vals)
            return root

        return make(l,r,tre)
