class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minX=m
        minY=n
        
        for i,j in ops:
            minX=min(minX,i)
            minY=min(minY,j)
            
        return minX*minY