class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
#         l=1
#         for r in range(1,len(nums)):
#             if nums[r-1]!=nums[r]:
#                 nums[l]=nums[r]
#                 l+=1
#         return l
        
        # or
        
        l=0
        for i in range(1,len(nums)):
            if nums[l] != nums[i]:
                l+=1
                nums[l]=nums[i]
        return l+1