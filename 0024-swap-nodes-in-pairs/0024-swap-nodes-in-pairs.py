# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode(0,head)
        curr=dummy
        
        while curr.next and curr.next.next:
            
            temp1=curr.next
            temp2=curr.next.next
            curr.next=temp2
            temp1.next=temp2.next
            temp2.next=temp1

# we're basically swapping and the main part is when we do temp1.next =temp2.next and we do it before we change temp2.next and this would not be a problem though in python the universal ans would be like this 

            curr=temp1
        
        return dummy.next
            
        