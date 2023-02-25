class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
#         l,r=0,len(nums)-1
        
#         while(l<=r):
#             mid=(l+r)//2
            
#             if target>nums[mid]:
#                 l=mid+1
#             elif target<nums[mid]:
#                 r=mid-1
#             else:
#                 return mid
        
#         return l
    
    
    
        l=0
        r=len(nums)
        
        while(l<r):
            m=(l+r)//2
            
            if nums[m]>=target:
                r=m
            else:
                l=m+1
        
        return l