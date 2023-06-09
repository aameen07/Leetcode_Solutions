# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev=cur=ListNode(0,head)
        while head:
            if head.next and head.val==head.next.val:
                while head.next and head.val==head.next.val:
                    head=head.next
                prev.next=head.next
            else:
                prev=prev.next
            head=head.next
        return cur.next

        
#         while head and head.next:
#             if head.val == head.next.val:
#                 while head and head.next and head.val==head.next.val:
#                     head=head.next
#                 head=head.next
#                 cur.next=head
#             else:
#                 cur=cur.next
#                 head=head.next
#         return pre.next