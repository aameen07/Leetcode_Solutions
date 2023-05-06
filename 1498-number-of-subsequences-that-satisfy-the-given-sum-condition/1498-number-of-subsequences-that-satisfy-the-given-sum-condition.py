class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
#         nums.sort()
#         l=0
#         r=len(nums)-1
#         c=0
#         mod=10**9+7
#         while l<=r:
#             if nums[l]+nums[r] <= target:
#                 c+=pow(2,r-l,mod)
#                 # c+=(2**(r-l))%mod
#                 l+=1
#             else:
#                 r-=1               
        
#         return c % mod
    
        
        # or
        
        
        i=0
        j=len(nums)-1
        nums.sort()
        c=0
        mod=10**9+7
        pows=[1]*len(nums)
        for k in range(1,len(nums)):
            pows[k]=(pows[k-1]*2)%mod
        while i<=j:
            if nums[i]+nums[j]<=target:
                c+=pows[j-i]%mod
                i+=1
            else:
                j-=1
        return c % mod
        
        