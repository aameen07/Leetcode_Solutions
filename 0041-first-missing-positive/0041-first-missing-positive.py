class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        i=0
        res=0
        for i in range(len(nums)):
            
            while 0<nums[i]<=len(nums) and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
            
        for j in range(len(nums)):
            if j+1 != nums[j]:
                return j+1
            
        return len(nums)+1
        