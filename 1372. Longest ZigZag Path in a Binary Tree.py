# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxval = 0
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root,right,left):
            if not root:
                return
            self.maxval = max(self.maxval,left,right)
            dfs(root.left,0,right+1)
            dfs(root.right,left+1,0)
        dfs(root,0,0)
        return self.maxval 
