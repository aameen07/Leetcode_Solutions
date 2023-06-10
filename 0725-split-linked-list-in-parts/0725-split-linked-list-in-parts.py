# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length=0
        node=head
        while node:
            node=node.next
            length+=1
        res=[[] for _ in range(k)]
        
        size,extra=length//k,length%k
        
        prev,cur=None,head
        
        for i in range(k):
            res[i]=cur
            for j in range(size + (1 if extra>0 else 0)):
                prev=cur
                cur=cur.next
            if prev: prev.next=None
            extra-=1
        
        return res

        