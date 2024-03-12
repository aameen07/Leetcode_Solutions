class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        return min(text.count("b"),text.count("a"),text.count("l")//2,text.count("o")//2,text.count("n"))
        
        
        # Or
        
        
#         a=['b','a','l','o','n']
#         b=[text.count(i) for i in a]
        
#         c=0
#         while True:
#             if b[0]>=1 and b[1]>=1 and b[2]>=2 and b[3]>=2 and b[4]>=1:     
#                 b=b[0]-1, b[1]-1, b[2]-2, b[3]-2, b[4]-1
#                 c+=1
#             else:
#                 break
#         return c

