class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        d=collections.defaultdict(int)
        
        for i in range(lowLimit,highLimit+1):
            val = 0
            
            while i>=1:
                val+=i%10
                i//=10
            
            d[val]+=1
        
        return max(d.values())
            
        