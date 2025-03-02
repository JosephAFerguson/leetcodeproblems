# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        while l1:
            num1.append(str(l1.val))
            l1 = l1.next
        while l2:
            num2.append(str(l2.val))
            l2 = l2.next
        num1 = num1[::-1]
        num2 = num2[::-1]
        num1s = ''.join(num1)
        num2s = ''.join(num2)
        res = str(int(num1s) + int(num2s))
        resl = []
        for i in res:
            resl.append(i)
        resl = resl[::-1]
        def buildtree(i):
            if i > len(resl)-1:
                return
            else:
                return ListNode(resl[i], buildtree(i+1))
        res = buildtree(0)
            
        return res
