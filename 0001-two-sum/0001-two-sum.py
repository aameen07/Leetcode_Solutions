class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):            #O(n**2)
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
                 
            # or
        
        d={}
        for i in range(len(nums)):
            if target - nums[i] in d:                   #O(n)
                return [d[target - nums[i]],i]
            d[nums[i]]=i
     