# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []
        def dfs(root,curr):
            if not root:
                return
            if not root.left and not root.right:
                curr.append(root.val)
            dfs(root.left,curr)
            dfs(root.right,curr)
            return curr
        leaf1 = dfs(root1,[])
        leaf2 = dfs(root2,[])
        return leaf1==leaf2
