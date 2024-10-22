# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, depth, h):
        if not root:
            return 
        if h.get(depth,-1) != -1:
            h[depth] += root.val
        else:
            h[depth] = root.val
        self.dfs(root.left, depth+1, h)
        self.dfs(root.right, depth+1, h)
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        h = {}
        self.dfs(root, 0, h)
        try:
            return sorted(h.values())[-k]
        except:
            return -1
