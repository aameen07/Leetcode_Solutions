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

# hum dic banaenge jaise jaise aage iterate krenge nums mei and hum check krenge target mei se abhi ka element subtract krke ke jo res aega wo hai kya dic mei and ni hoga to abhi wale element ko key bana kr uska index value pr dal denge and aage check krenge until we find the target.