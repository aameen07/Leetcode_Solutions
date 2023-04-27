class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        lsum=0
        rsum=sum(nums)-nums[0]
        
        for i in range(len(nums)):
            
            if lsum==rsum:
                return i
            elif i+1==len(nums):
                rsum=0
            else:
                lsum+=nums[i]
                rsum-=nums[i+1]
        
        return -1
                
        
        