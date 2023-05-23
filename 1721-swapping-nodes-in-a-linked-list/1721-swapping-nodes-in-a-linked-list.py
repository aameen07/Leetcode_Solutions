# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
#         curr=head
#         c=0
#         arr=[]
#         while curr:
#             arr.append(curr.val)
#             curr=curr.next
#             c+=1
        
#         arr[k-1],arr[c-k]=arr[c-k],arr[k-1]
        
#         curr=head
#         i=0
#         while i!=c:
#             curr.val=arr[i]
#             curr=curr.next
#             i+=1
        
#         return head

                # or
        
        curr = head
        for _ in range(k-1):
            curr = curr.next
        first = curr
        
        second = head
        while curr.next:
            curr = curr.next
            second = second.next
        
        first.val, second.val = second.val, first.val
        
        return head
        
        
        
        
        
        