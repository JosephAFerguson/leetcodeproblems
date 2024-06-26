# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    r= 0
    def dfs(self, root, currP):
        #make sure we do not add any node paths that have children
        if not root:
            return
        currP += str(root.val)
        self.dfs(root.left, currP)
        self.dfs(root.right, currP)
        if not root.left and not root.right:
            self.r+=int(currP)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.r = 0
        self.dfs(root,"")
        return self.r
