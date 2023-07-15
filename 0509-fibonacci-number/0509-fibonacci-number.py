class Solution:
    def fib(self, n: int) -> int:
        def fibn(n,dp):
            if n==0: return 0
            elif n==1: return 1
            elif dp[n]!=-1: return dp[n]
            dp[n]=fibn(n-1,dp)+fibn(n-2,dp)
            return dp[n]
            
        dp=[-1]*(n+1)
        res=fibn(n,dp)
        return res