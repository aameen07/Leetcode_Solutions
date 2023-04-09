class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
    
        curr=maxx=nums[0]
        
        for r in range(1,len(nums)):
            
            curr=max(nums[r],curr+nums[r])
            maxx=max(curr,maxx)
            
        return maxx
        
        