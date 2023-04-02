class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        mini=float('inf')
        l=0
        r=k-1
        
        while(r<len(nums)):
            mini=min(nums[r]-nums[l],mini)    
            l+=1
            r+=1
        
        return mini
            
        