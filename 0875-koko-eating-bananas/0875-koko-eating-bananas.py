class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

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
    
        