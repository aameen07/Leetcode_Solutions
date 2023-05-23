# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
#         dummy2=dummy=ListNode(0,head)
#         curr=head
        
#         for _ in range(n-1):
#             curr=curr.next
        
#         while curr.next:
#             curr=curr.next
#             dummy=dummy.next
        
#         dummy.next=dummy.next.next
        
#         return dummy2.next
                
                # or
        
        l=d=ListNode(0,head)
        curr=head
        while curr.next:
            if n>1:
                n-=1
            else:
                d=d.next
            curr=curr.next
        
        d.next=d.next.next
        
        return l.next
        