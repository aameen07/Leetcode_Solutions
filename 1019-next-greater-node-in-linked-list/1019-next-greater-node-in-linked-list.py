# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        l=[]
        
        cur=head
        while cur:
            l.append(cur.val)
            cur=cur.next
        
        arr=[0]*len(l)
        stack=[]
        
        for i,val in enumerate(l):      
            while stack and l[stack[-1]]<val:
                arr[stack.pop()]=val        
                
            
            stack.append(i)        
        
        return arr