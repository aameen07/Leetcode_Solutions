class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        l=0
        r=n-1
        s=[-1]*2
        
        while(l<=r):
            m=(l+r)//2
            
            if nums[m] == target:
                s[0]=m
                r=m-1
            
            elif target > nums[m]:
                l=m+1
                
            elif target<nums[m]:
                r=m-1

        
        l=0
        r=n-1
        while(l<=r):
            m=(l+r)//2
            
            if target == nums[m]:
                s[1]=m
                l=m+1
            
            elif target>nums[m]:
                l=m+1
                
            elif target<nums[m]:
                r=m-1
            
        
        return s