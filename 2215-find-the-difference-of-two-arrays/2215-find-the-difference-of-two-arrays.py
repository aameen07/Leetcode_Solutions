class Solution:
    def findDifference(self, n1: List[int], n2: List[int]) -> List[List[int]]:
        
#         a=[]
#         b=[]
#         res=[]
#         for i,val in enumerate(n1):
#             if val not in n2:
#                 a.append(val)
        
#         for i,val in enumerate(n2):
#             if val not in n1:
#                 b.append(val)
            
#         res.append(set(a))
#         res.append(set(b))
#         return res
        
        # or
        
        
        n1,n2=set(n1),set(n2)
        return [list(n1-n2),list(n2-n1)]
        