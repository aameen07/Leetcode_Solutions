class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
                
                    
#         i=0
#         while(i<len(nums)):
#             if nums[i]+nums[i+1] == target:
#                 return [i,i+1]
            
#             i+=1
        
        d={}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target - nums[i]],i]
            
            
            d[nums[i]]=i
            