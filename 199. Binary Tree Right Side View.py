# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        depth = 1
        vals = []
        def dfs(root,depth):
            if not root:
                return
            if len(vals) < depth:
                vals.append(root.val)

            dfs(root.right,depth+1)
            dfs(root.left,depth+1)
        dfs(root,depth)
        return vals

