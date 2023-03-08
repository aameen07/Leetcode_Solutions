class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         l=ceil(sum(piles)/h)
#         r=max(piles)
        
#         while (l<r):
#             m=(l+r)//2
#             total_time=0
            
#             for i in piles:
#                 total_time=ceil(i/m)
                
#                 if total_time>h:
#                     break
            
#             if total_time<=h:
#                 r=m
#             else:
#                 l=m+1
#         return r

        l=1
        r= max(piles)
        while(l<r):
            m=(l+r)//2
            c=0
            
            for i in piles:
                c+=((i-1)//m)+1
            
            if c>h:
                l=m+1
            else:
                r=m
        
        return r
    
        