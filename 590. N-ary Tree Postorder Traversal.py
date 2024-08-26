"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    li = []
    def post(self, root):
        if not root:
            return
        for i in root.children:
            self.post(i)
        self.li.append(root.val)
    def postorder(self, root: 'Node') -> List[int]:
        self.li = []
        self.post(root)
        return self.li
