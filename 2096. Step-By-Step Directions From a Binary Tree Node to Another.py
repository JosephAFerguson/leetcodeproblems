# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(root,tar, path):
            if root.val == tar:
                return True
            if root.left and find(root.left, tar,path):
                path+='L'
            elif root.right and find(root.right, tar, path):
                path+='R'
            return path
        p1,p2 = [],[]
        find(root,startValue,p1)
        find(root,destValue,p2)
        while p1 and p2 and p1[-1]==p2[-1]:
            p1.pop()
            p2.pop()
        return ("U"*len(p1))+"".join(p2[::-1])
