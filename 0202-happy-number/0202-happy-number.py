class Solution:
    def isHappy(self, n: int) -> bool:
        
#         if n==1:
#             return True
        
#         if n//10==0:
#             return False
        rem=set()
        
        while(n!=1):
            total=sum([int(i)**2 for i in str(n)])
            if total in rem:
                return False
            rem.add(total)
            n=total
        
        else:
            return True