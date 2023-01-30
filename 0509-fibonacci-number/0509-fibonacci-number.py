class Solution:
    def fib(self, n: int) -> int:
        
        dp = [0]*(n+1) # we are creating dp array of length 1 greater than the length of fibonacci                          series we're supposed to return  
        
        if n<=1: return n
        
        dp[1]=1
        
        for i in range(2, len(dp)): # here len(dp) is n+1 in size
            dp[i]=dp[i-1]+dp[i-2]  #we take the previous two values of the dp to get the new value                                      of dp
            
        return dp[-1]