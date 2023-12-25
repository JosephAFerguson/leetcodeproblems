# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        snake = []
        def build(root):
            if not root:
                return
            build(root.left)
            snake.append(root.val)
            build(root.right)
        build(root)
        for i,val in enumerate(snake):
            if i < len(snake)-1:
                if snake[i+1] <= val:
                    return False

        return True
