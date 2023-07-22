class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # if d[-1] != 9:
        #     d[-1]+=1
        #     return d
        # elif len(d)==1 and d[-1] == 9:
        #     return [1,0]
        # else:
        #     d[-1]=0
        #     d[0:-1] = self.plusOne(d[0:-1])
        #     return d
        
        # or
        
        b=""
        for i in digits:
            b+=str(i)
        b=str(int(b)+1)
        c=[int(j) for j in b]
        return c
                