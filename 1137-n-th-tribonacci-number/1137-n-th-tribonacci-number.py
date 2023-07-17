class Solution:
    def tribonacci(self, n: int) -> int:
        
#         dp=[0]*(n+1)
#         if n==0: return 0
#         if n<3: return 1
        
#         dp[1]=1
#         dp[2]=1
        
#         for i in range(3,n+1):
#             dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
            
#         return dp[n]
    
        # or
        
        
        a,b,c= 0,1,1
        if n<2: return n
        
        for i in range(3,n+1):
            d=a+b+c
            a=b
            b=c
            c=d
        
        return c