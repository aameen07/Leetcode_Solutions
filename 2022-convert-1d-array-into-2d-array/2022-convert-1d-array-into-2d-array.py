class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res=[]
        
        if len(original) == m*n:
            for i in range(0,m*n,n):
                res.append(original[i:i+n])
        return res