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
        
        if not head: return None
        
        #find middle
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        mid=slow
        
        #reverse second half
        prev=None
        nxt=None
        
        while mid:
            nxt=mid.next
            mid.next=prev
            prev=mid
            mid=nxt
        
        
        #merge lists
        h1=head
        h2=prev
        
        while h2.next:
            n1=h1.next
            n2=h2.next
            
            h1.next=h2
            h2.next=n1
            
            h1=n1
            h2=n2
            
            
        return head
            
        