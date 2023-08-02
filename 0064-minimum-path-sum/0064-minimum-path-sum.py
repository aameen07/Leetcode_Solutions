class Solution:
    def minPathSum(self, dp: List[List[int]]) -> int:
        r=len(dp)
        c=len(dp[0])
        
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                
                if i==r-1 and j==c-1:
                    continue
                    
                elif i==r-1:
                    dp[i][j] += dp[i][j+1]
                elif j==c-1:
                    dp[i][j] += dp[i+1][j]
                else:
                    dp[i][j] = min(dp[i][j]+dp[i+1][j],dp[i][j]+dp[i][j+1])
        
        return dp[0][0]