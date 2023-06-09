# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        pre=cur=ListNode(0,head)
        # pre.next=head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val==head.next.val:
                    head=head.next
                head=head.next
                cur.next=head
            else:
                cur=cur.next
                head=head.next
        return pre.next
            
#         dummy = pre = ListNode(0)
#         dummy.next = head
#         while head and head.next:
#             if head.val == head.next.val:
#                 while head and head.next and head.val == head.next.val:
#                     head = head.next
#                 head = head.next
#                 pre.next = head
#             else:
#                 pre = pre.next
#                 head = head.next
#         return dummy.next