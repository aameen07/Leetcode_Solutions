class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums)==1:
            return True
        
        jump=nums[0]
        
        for i in range(1,len(nums)):
            if jump==0:
                return False
            jump-=1
            jump=max(jump,nums[i])
        return True
            
        