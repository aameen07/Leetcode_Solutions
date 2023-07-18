class Solution:
    def generate(self, n: int) -> List[List[int]]:
#         dp=[[1]*(i+1) for i in range(n)]
        
#         for i in range(n):
#             for j in range(1,i):
#                 dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            
#         return dp
    
    # or
    
        res=[]
        prev=[]
        for i in range(n):
            nums = []
            j=0
            while (j<=i):
                if j==0 or j==i:
                    nums.append(1)
                else:
                    nums.append(prev[j-1]+prev[j])
                j+=1
            prev=nums
            res.append(nums)
        
        return res
            
                    