class Solution:
    def trap(self, height: List[int]) -> int:
        
        l=0
        r=len(height)-1
        L=0
        R=0
        total=0
        
        while(l<r):
            
            L=max(L,height[l])
            R=max(R,height[r])
            
            if L<=R:
                total+=L-height[l]
                l+=1
            
            else:
                total+=R-height[r]
                r-=1
        
        return total
            
        