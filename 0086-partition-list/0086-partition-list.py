# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur=head
        a1=ListNode(0)
        a2=ListNode(0)
        dummy1=a1
        dummy2=a2
        while cur:
            if cur.val<x:
                a1.next=cur
                a1=a1.next
                
            elif cur.val>=x:
                a2.next=cur
                a2=a2.next
            cur=cur.next
        
        
        a1.next=dummy2.next
        a2.next=None
        return dummy1.next