# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        def dfs(root,curr):
            if not root:
                return

            curr+=(root.val)

            if curr == targetSum:
                self.res +=1 
            self.res += h[curr-targetSum]
            h[curr] += 1 
            dfs(root.left,curr)
            dfs(root.right,curr)
            h[curr]-=1

        h = defaultdict(int)
        dfs(root,0)
        return self.res
