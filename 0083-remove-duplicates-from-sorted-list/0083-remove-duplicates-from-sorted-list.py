# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        
        curr=head
        nxt=head.next
        
        while nxt:
            if curr.val==nxt.val:
                nxt=nxt.next
            else:
                curr.next=nxt
                curr=curr.next
                nxt=nxt.next
        
        curr.next=None
        return head
        
        
        # or
        
        
#         curr=head
        
#         while curr and curr.next:
#             if curr.val==curr.next.val:
#                 curr.next=curr.next.next
#             else:
#                 curr=curr.next
        
#         return head