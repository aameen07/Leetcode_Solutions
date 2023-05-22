# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        
        
#         while nxt:
#             if count==a:
#                 curr.next=list2
#                 break
#             else:
#                 curr=curr.next
#                 nxt=nxt.next
#                 count+=1
        
#         while nxt:
#             if count==b:
#                 nxt=nxt.next
#                 break
#             else:
#                 nxt=nxt.next
#                 count+=1
        
#         while curr.next:
#             curr=curr.next
        
#         curr.next=nxt
        
#         return list1
    
    
        # or
        
        
        curr=nxt=list1
        count=0
        
        while count!=a-1:
            curr=curr.next
            nxt=nxt.next
            count+=1
        
        while count!=b+1:
            nxt=nxt.next
            count+=1
        
        curr.next=list2
        
        while curr.next:
            curr=curr.next
        
        curr.next=nxt
        
        return list1
            
            
            
            
            
            
        
        
        
        
        
        