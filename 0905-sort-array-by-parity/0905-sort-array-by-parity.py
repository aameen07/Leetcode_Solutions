class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
#         l=0
#         for r in range(1,len(nums)):
            
#             if (nums[l]%2==0):
#                 l+=1
            
#             elif nums[l]%2!=0 and nums[r]%2==0:
#                 nums[l],nums[r]=nums[r],nums[l]
#                 l+=1
                
#         return nums
        
        # we try to get the left as odd for that we used the if condition and for getting the swap condition possible we used the elif condition
        
        
        l,r=0,0
        
        while(r<len(nums)):
            if nums[r]%2==0:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
            r+=1
        
        return nums
        