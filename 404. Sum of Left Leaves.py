# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    r = 0
    def dfs(self,root, l):
        if not root:
            return 
        self.dfs(root.left, True)
        if not root.left and not root.right and l:
            self.r+=root.val
        self.dfs(root.right, False)
        
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.r = 0
        self.dfs(root, False)
        return self.r
