class Solution:
    def climbStairs(self, n: int) -> int:
        
        #0,1,1,2,3,5,8,13,21,34,55
        
        dp = [0]*(n+1)
        dp[0] = 1
        
        for i in range(1,len(dp)):
            dp[i] = dp[i-1]+dp[i-2] 
            
        return dp[-1]
            
        