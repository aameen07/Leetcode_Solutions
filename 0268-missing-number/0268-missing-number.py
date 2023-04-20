class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n=len(nums)
        
        i=0
        res=0
        for i in range(len(nums)):
            while nums[i]<len(nums) and i!=nums[i]:
                nums[nums[i]],nums[i]=nums[i],nums[nums[i]]
            
        for j in range(len(nums)):
            if j != nums[j]:
                return j
            
        return j+1
        
        