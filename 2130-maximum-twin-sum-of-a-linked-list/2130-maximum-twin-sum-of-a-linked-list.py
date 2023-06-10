# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur=head
        l=[]
        maxVal=0
        
        while cur:
            l.append(cur.val)
            cur=cur.next
        
        n=len(l)
        i=0
        while i<n:
            maxVal=max(maxVal,l[i]+l[n-1-i])    
            i+=1
        
        return maxVal
        
        
        
        
        
        
        
#         slow,fast=head,head
#         maxVal=0
        
#         while fast and fast.next:
#             slow=slow.next
#             fast=fast.next.next
            
#         cur,prev=slow,None
#         while cur:
#             nxt=cur.next
#             cur.next=prev
#             prev=cur
#             cur=nxt

#         while prev:
#             maxVal=max(maxVal,head.val+prev.val)
#             prev=prev.next
#             head=head.next

#         return maxVal