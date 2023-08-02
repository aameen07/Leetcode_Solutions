class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        
        m=len(g)
        n=len(g[0])
        
        dp =[[0]*n for _ in range(m)]
        if g[m-1][n-1]==1:
            return 0
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i== m-1 and j==n-1:
                    dp[i][j]=1
                
                elif g[i][j] == 1:
                    dp[i][j]=0
                    
                elif i==m-1:
                    dp[i][j]=dp[i][j+1]
                
                elif j==n-1:
                    dp[i][j]=dp[i+1][j]
                    
                else:
                    dp[i][j] = dp[i+1][j]+dp[i][j+1]
        
        return dp[0][0]