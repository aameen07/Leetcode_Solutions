class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        
        if d[-1] != 9:
            d[-1]+=1
            return d
        elif len(d)==1 and d[-1] == 9:
            return [1,0]
        else:
            d[-1]=0
            d[0:-1] = self.plusOne(d[0:-1])
            return d