# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        L=dummy=ListNode(0,head)
        curr=head
        
        for _ in range(n-1):
            curr=curr.next
        
        
        while curr.next:
            curr=curr.next
            dummy=dummy.next
        
        dummy.next=dummy.next.next
        
        return L.next
        
        