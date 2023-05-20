# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr=head
        nxt=head.next
        s=0
        
        while nxt:    
            if nxt.val!=0:
                s+=nxt.val
            else:
                curr=curr.next
                curr.val=s
                s=0
            nxt=nxt.next
        
        curr.next=None
        return head.next