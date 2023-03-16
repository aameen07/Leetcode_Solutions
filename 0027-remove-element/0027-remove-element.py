class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

                
#         l=0
#         r=len(nums)-1
        
#         while(l<=r):
#             if nums[l]==val:
#                 nums[l],nums[r]=nums[r],nums[l]
#                 r-=1
#             else:
#                 l+=1
#         return l
        
    # or 
    
        l=0
        r=0
        
        while(r<len(nums)):
            
            if nums[r]!=val:
                nums[l] = nums[r]
                l+=1
            r+=1
        return l

