class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        res=0
        total=0
        
        for i, num in enumerate(nums):
            total+=num
            res= max(res,math.ceil(total/(i+1)))
        
        return res
            
            
            
        