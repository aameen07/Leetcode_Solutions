class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        
#         if d[-1] != 9:
#             d[-1]+=1
#             return d
#         elif len(d)==1 and d[-1] == 9:
#             return [1,0]
#         else:
#             d[-1]=0
#             d[0:-1] = self.plusOne(d[0:-1])
#             return d
        
#         # or
        
#         b=""
#         for i in d:
#             b+=str(i)
#         b=str(int(b)+1)
#         c=[int(j) for j in b]
#         return c
                
    # or
    
        for i in range(len(d)-1, -1, -1):
            if d[i] != 9:
                d[i] += 1
                break
            else:
                d[i] = 0
        if d[0] == 0:
            d.insert(0, 1)
        return d