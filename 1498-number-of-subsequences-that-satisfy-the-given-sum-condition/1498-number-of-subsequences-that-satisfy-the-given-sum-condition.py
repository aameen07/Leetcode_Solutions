class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        l=0
        r=len(nums)-1
        c=0
        mod=10**9+7
        while l<=r:
            if nums[l]+nums[r] <= target:
                c+=pow(2,r-l,mod)
                l+=1
            else:
                r-=1
        # while l<=r:
        #     if nums[l]+nums[r] > target:
        #         r-=1
        #     else:
        #         c+=pow(2,r-l,mod)
        #         l+=1            
        
        return c%mod
    
    