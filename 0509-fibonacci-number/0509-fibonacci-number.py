class Solution:
    def fib(self, n: int) -> int:
        def fibn(n,dp):
            if dp[n]!=0: return dp[n]
            elif n==0: return 0
            elif n==1: return 1
            
            dp[n]=fibn(n-1,dp)+fibn(n-2,dp)
            return dp[n]
            
        dp=[0]*(n+1)
        res=fibn(n,dp)
        return res