class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m=matrix
        
        for i in range (len(m)):
            for j in range(i+1,len(m)):
                
                m[i][j],m[j][i]=m[j][i],m[i][j] # pehla column ab pehli row ban jaega 
        
        for i in range(len(m)):
            m[i] = m[i][::-1]   # hum har ek row ko reverse kr denge and we get ans
        