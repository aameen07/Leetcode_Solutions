class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
#         d={}
        
#         for i in s:
#             if i in d:
#                 d[i]+=1
#             else:
#                 d[i]=1
        
#         a=d[s[0]]
        
#         for j in d:
#             if a!=d[j]:
#                 return False
        
#         return True
            
            
            # or
        return len(set(Counter(s).values())) == 1
            