# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        
        while len(lists)>1:
            ansList=[]
            for i in range(0,len(lists),2):
                a=lists[i]
                if i+1<len(lists):
                    b=lists[i+1]
                else:
                    b=None
                c=self.merge(a,b)
                ansList.append(c)
            lists=ansList
        return lists[0]
        
    def merge(self,l1,l2):
        res=ListNode()
        cur=res
        while l1 and l2:
            if l1.val<l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        if l1:                  
            cur.next=l1         
        if l2:
            cur.next=l2
        return res.next
        
        
        