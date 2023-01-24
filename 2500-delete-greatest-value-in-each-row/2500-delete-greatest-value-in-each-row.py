class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        res=0
        for j in range(n):
            maxx=0
            for i in range(m):
                a=max(grid[i])
                maxx = max(a,maxx)
                grid[i].remove(a)
            res+=maxx
        
        return res
    

                
                