# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = []
        def dfs(root):
            if not root:
                return
            stack.append(root.val)
            dfs(root.right)
            dfs(root.left)
        dfs(root)
        res = 0
        for i in stack:
            if i >= low and i <= high:
                res+=i
        return res
