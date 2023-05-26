# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        tmp=head
        c=0
        while tmp and c<k:
            tmp=tmp.next
            c+=1
        
        if c<k:
            return head
        
        
        dummy=head
        prev=None
        nxt=None
        curr=head
        
        for i in range(k):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        dummy.next=self.reverseKGroup(curr,k)
        
        return prev