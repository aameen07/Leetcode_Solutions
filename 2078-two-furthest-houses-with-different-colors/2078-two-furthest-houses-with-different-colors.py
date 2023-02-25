class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        
        l=colors[0]
        r=colors[-1]
        res=0
        
        for i in range(len(colors)):
            
            if l!=colors[i]:
                res= max(res,i)
            
            if colors[i]!=r:
                res= max(len(colors)-1-i,res)
            
        return res