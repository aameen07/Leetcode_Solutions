class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        # we have to make a dict and use the count and then check the count if it is multiple of 2
        
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        # ive got count now
        
        for i in d:
            # print(d[i])
            if (d[i]%2) != 0:
                return False
        
        return True