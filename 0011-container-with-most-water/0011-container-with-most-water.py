class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l=0
        r=len(height)-1
        
        area=float("-inf")
        
        while l<r:
            b=r-l
            h=min(height[l],height[r])
            area=max(area,h*b)
            
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        
        return area
        
# 