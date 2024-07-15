# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        h = {}
        h2 = {}
        for par, child, isL in descriptions:
            h[child] = par
            if h2.get(par):
                h2[par].append([child, isL])
            else:
                h2[par] = [[child,isL]]
        i = list(h.keys())[0]
        while h.get(i, 0):
            i = h[i]
        res = TreeNode(i)
        def create(root, vals,has):
            if not root:
                return
            if len(vals)>1:
                if vals[0][1]:
                    root.left = TreeNode(vals[0][0])
                    root.right = TreeNode(vals[1][0])
                    if has.get(vals[0][0]):
                        create(root.left, has[vals[0][0]], has)
                    if has.get(vals[1][0]):
                        create(root.right, has[vals[1][0]], has)
                else:
                    root.left = TreeNode(vals[1][0])
                    root.right = TreeNode(vals[0][0])
                    if has.get(vals[1][0]):
                        create(root.left, has[vals[1][0]], has)
                    if has.get(vals[0][0]):
                        create(root.right, has[vals[0][0]], has)
            else:
                if vals[0][1]:
                    root.left = TreeNode(vals[0][0])
                    root.right = None
                    if has.get(vals[0][0]):
                        create(root.left, has[vals[0][0]], has)
                else:
                    root.left = None
                    root.right = TreeNode(vals[0][0])
                    if has.get(vals[0][0]):
                        create(root.right, has[vals[0][0]], has)
        create(res, h2[i], h2)
        return res
