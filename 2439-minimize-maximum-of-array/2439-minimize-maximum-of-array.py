class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        res=0
        prefixsum=0
        
        for i, num in enumerate(nums):
            prefixsum+=num
            res= max(res,math.ceil(prefixsum/(i+1)))
        
        return res
            
            
            
        