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

        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if sum((p + m - 1) // m for p in piles) > h:
                l = m + 1
            else:
                r = m
        return l
            
            