class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res=[1]*len(nums)
        
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        
        return res
    
    
# We simply first entered the prefix multiplicated values in the result array from the second postion then we took the postfix multiplicated values and multiplied them with the result array values from the end postion going backwards this gave us the result array which we needed according to the question.