class Solution:
    def fib(self, n: int) -> int:
        
        dp=[0]*(n+1)
        if n<=1: return n
        dp[n]=self.fib(n-1)+self.fib(n-2)
        return dp[n]
        