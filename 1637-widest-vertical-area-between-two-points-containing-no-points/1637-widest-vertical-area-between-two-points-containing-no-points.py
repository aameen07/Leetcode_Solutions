class Solution:
    def maxWidthOfVerticalArea(self, p: List[List[int]]) -> int:
        
        p.sort()
        res=0
        for i in range(1,len(p)):
            res=max(p[i][0]-p[i-1][0],res)
        return res
            
            