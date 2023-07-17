# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        # dummy=None
        # dummy=ListNode(7,dummy)
        # dummy=ListNode(0,dummy)
        s1=[]
        s2=[]
        while l1 or l2:
            if l1:
                s1.append(l1.val)
                l1=l1.next
            if l2:
                s2.append(l2.val)
                l2=l2.next
        
        carry=0
        dummy=None
        while s1 or s2 or carry:
            v1=v2=0
            if s1: v1=s1.pop()
            if s2: v2=s2.pop()
            carry,value=divmod(v1+v2+carry,10)            
            dummy=ListNode(value,dummy)
        
        return dummy
        
        
        
        
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        