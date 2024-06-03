# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxv = 0
    def dfs(self,root,depth):
        left = self.dfs(root.left, depth+1) if root.left else 0
        right = self.dfs(root.right, depth +1) if root.right else 0
        self.maxv = max(left + right, self.maxv)
        return 1 + max(left,right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxv = 0   
        self.dfs(root, 0)
        return self.maxv

