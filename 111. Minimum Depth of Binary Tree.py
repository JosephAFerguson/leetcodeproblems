# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,depth):
        if not root:
            return 9999999999
        if not root.right and not root.left:
            return depth
        return min(self.dfs(root.right, depth+1), self.dfs(root.left, depth+1))
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.dfs(root, 1)
