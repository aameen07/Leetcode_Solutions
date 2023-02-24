class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
#         l=0
        
#         for r in range(len(nums)):
            
#             if nums[r]!=val:
#                 nums[l] = nums[r]
#                 l+=1

#         return l

# or
        l=0
        r=len(nums)-1
        
        while(l<=r):
            if nums[l]==val:
                a=nums[r]
                nums[r]=nums[l]
                nums[l]=a
                
                r-=1
            
            else:
                l+=1
        
        return l
        