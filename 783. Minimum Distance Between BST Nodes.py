# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        stack = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            stack.append(root.val)
            dfs(root.right)
        
        dfs(root)
        mindif = 999999
        for i in range(len(stack)-1):
            mindif = min(mindif, stack[i+1]-stack[i])
        return mindif
