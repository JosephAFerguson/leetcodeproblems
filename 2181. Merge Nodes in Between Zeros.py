# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp.next:
            t2 = temp.next
            if temp.val == 0:
                s = 0
                while t2.val!=0:
                    s+= t2.val
                    t2 = t2.next     
                temp.val = s
                temp.next = t2
            if not temp.next.next:
                temp.next = None
                break
            temp = temp.next
        
        return head           
