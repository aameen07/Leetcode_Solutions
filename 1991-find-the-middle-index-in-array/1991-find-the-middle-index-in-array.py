class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        lsum=0
        rsum=sum(nums)
        
        for i,val in enumerate(nums):
            
            rsum-=val
            if lsum==rsum:
                return i
            lsum+=val 
        
        return -1
                
        
        