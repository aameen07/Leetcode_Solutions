class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        c=0
        a=set(nums)
        for i in range(len(a)):
            if nums[i]+diff in a and nums[i]+ 2*diff in a:
                c+=1
        
        return c
            
#         count = 0
#         for i in nums:
#             if (i+diff) in nums and (i+(2*diff)) in nums:
#                 count+=1
        
#         return count
    
        
        