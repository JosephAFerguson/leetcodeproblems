# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            vals.append(root.val)
            dfs(root.right)
        dfs(root)
        def build(l,r):
            if l>r:
                return None
            mid = (l+r)//2
            root = TreeNode(vals[mid])
            root.left, root.right = build(l,mid-1), build(mid+1,r)
            return root
        return build(0,len(vals)-1)
        
        return None
