# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
#         ans=0
#         cur=head
#         count=0
        
#         while cur:
#             count+=1
#             cur=cur.next
        
#         cur=head
#         while cur:
#             ans+=2**(count-1) * cur.val
#             count-=1
#             cur=cur.next
        
#         return ans

        # or
        
        
        ans=0
        while head:
            ans=2*ans+head.val
            head=head.next
        return ans
    