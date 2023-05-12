# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res=ListNode()          #This made a node with 0 val and None .next address
        cur=res                 #now i create a copy of the head
        
        while l1 and l2:        

            if l1.val<l2.val:
                cur.next=l1
                l1=l1.next
            
            else:
                cur.next=l2
                l2=l2.next
                
            cur=cur.next
        
        if l1:                  #If any list is not empty even now then we add its link only one time
            cur.next=l1         #cuz that will add the remaining linked list which got left
            
        if l2:
            cur.next=l2
        
        return res.next         #We give the .next address so that we can avoid that extra node that we 
                                #added in the start
        
        