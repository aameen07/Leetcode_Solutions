# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         l=[]
#         cur=head
#         while cur:
#             while l and cur.val>l[-1]:
#                 l.pop()
            
#             l.append(cur.val)
#             cur=cur.next
        
#         dummy=None
#         while l:
#             dummy=ListNode(l.pop(),dummy)
        
#         return dummy
        if not head:
            return None
        
        head.next = self.removeNodes(head.next)
        
        if head.next and head.val < head.next.val:
            return head.next
        
        return head