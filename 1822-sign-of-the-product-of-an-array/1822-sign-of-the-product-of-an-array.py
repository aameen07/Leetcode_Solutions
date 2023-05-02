class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod=1
        
        if 0 in nums:
            return 0
        
        for i in range(len(nums)):
            prod*=nums[i]
        
        
        return self.signFunc(prod)
        
    def signFunc(self, p):
        if p>0:
            return 1
        elif p==0:
            return 0
        else:
            return -1