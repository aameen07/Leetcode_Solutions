class Solution:
    def pivotInteger(self, n: int) -> int:
        
        asum=n*(n+1)//2
        # print(asum)
        bsum=0
        for i in range(1,n+1):
            bsum+=i
            if asum==bsum:
                return i
            else:
                asum-=i
        
        return -1
    
    
#         rsum=sum([i for i in range(1,n+1)])
#         lsum=0
#         for i in range(1,n+1):
#             lsum+=i
#             if lsum!=rsum:
#                 rsum-=i
#             else:
#                 return i
#         return -1
            
        
        
    
        
        