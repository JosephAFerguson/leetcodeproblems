# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    paths  = []
    def dfs(self, root, currP):
        #make sure we do not add any node paths that have children
        if not root:
            return
        currP += chr(root.val + 97)
        self.dfs(root.left, currP)
        self.dfs(root.right, currP)
        if not root.left and not root.right:
            self.paths.append(currP[::-1])
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.paths = []
        self.dfs(root, "")
        print(self.paths)
        least = "~~~"
        for i,val in enumerate(self.paths):
            least = min(val, least)

        return least
