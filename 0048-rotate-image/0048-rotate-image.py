class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m=matrix
        
        for i in range (len(m)):
            for j in range(i,len(m)):
                # 
                m[i][j],m[j][i]=m[j][i],m[i][j]
        
        for i in range(len(m)):
            m[i] = m[i][::-1]
        