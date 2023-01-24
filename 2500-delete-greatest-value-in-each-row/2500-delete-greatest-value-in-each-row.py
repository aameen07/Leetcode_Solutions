class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        res=0
        for _ in range(len(grid[0])):
            maxx=0
            for i in range(len(grid)):
                a=max(grid[i])
                maxx = max(a,maxx)
                grid[i].remove(a)
            res+=maxx
        
        return res
    
    

                
                