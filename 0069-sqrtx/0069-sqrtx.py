class Solution:
    def mySqrt(self, x: int) -> int:
        
        # l=0
        # r=x
        # while(l<=r):
        #     m=(l+r)//2
        #     if (m*m)<=x and ((m+1)*(m+1))>x:
        #         return m
        #     elif (m*m) > x:
        #         r=m-1        
        #     else:
        #         l=m+1
        
        
        
        l=0
        r=x
        
        if x==0 or x==1: return x
        
        while(l<r):
            m=(l+r)//2
            
            if (m*m) <= x:
                l=m+1    
            else:
                r=m
        
        return l-1
    
    
        #   r=m-1, r=m, l=m+1, return m  ye 4 hi scenerio honge kisi condition ke andr finally 95% questions mei