# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        # making Null of half linked list
        prev=slow.next=None
        # reverse the end linked list
        while second:
            nxt=second.next
            second.next=prev
            prev=second
            second=nxt
        # merging the divided linked list
        first,last=head,prev
        while last:
            nxt1,nxt2=first.next,last.next
            first.next=last
            last.next=nxt1
            first,last=nxt1,nxt2
