class Solution:
    def finalPrices(self, p: List[int]) -> List[int]:
        
        res=[]
        
        for i in range (len(p)):
            while res and p[i]<=p[res[-1]]:
                p[res.pop()]-=p[i]
            res.append(i)
        return p
        