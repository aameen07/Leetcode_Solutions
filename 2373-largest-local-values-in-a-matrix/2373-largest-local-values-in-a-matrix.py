class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        n=len(grid)
        ans = [[0] * (n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                largest=0
                for k in range(0,3):
                    for l in range(0,3):
                        largest=max(largest,grid[k+i][l+j])
                ans[i][j] = largest
                
        return ans
    
    
     # or
        
#         n=len(grid)
#         ans = [[0] * (n-2) for _ in range(n-2)]
#         for i in range(n-2):
#             for j in range(n-2):
#                 for k in range(i,i+3):
#                     for l in range(j, j+3):
#                         ans[i][j] = max(ans[i][j], grid[k][l])
                        
#         return ans
        
    
    