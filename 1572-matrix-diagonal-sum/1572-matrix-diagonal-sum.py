class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        count=0
        for i in range(len(mat)):
            count+=mat[i][i]
        
        c=len(mat[0])-1   
        r=0
        while(c>=0):
            count += mat[r][c]
            r+=1
            c-=1
        
        if len(mat)%2 != 0:
            return count-(mat[len(mat)//2][len(mat)//2])
        
        return count
        
            
#         sum=0
#         for i in range(len(mat)):
#             for j in range(0,len(mat[0])):
#                 if i==j or i+j==len(mat)-1:
#                     sum+=mat[i][j]
                
#         return sum