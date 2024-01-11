# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0

        def path(root,currmax,currmin):
            if not root:
                return currmax-currmin
            currmax = max(root.val, currmax)
            currmin = min(root.val, currmin)
            left = path(root.left,currmax,currmin)
            right = path(root.right,currmax,currmin)
            return max(left,right)
        return path(root,root.val,root.val)
