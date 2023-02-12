class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        if nums[0]>0 or nums[-1]<0:
            return len(nums)
        
        if set(nums)=={0}:
            return 0
        
        pos=0
        neg=0
        l=0
        r=len(nums)-1
        while (l<r):
            mid=(l+r)//2
            if nums[mid]>0:
                r=mid
            else:
                l=mid+1 
        pos=len(nums)-r

        
        l=0
        r=len(nums)-1
        while (l<r):
            mid=(l+r)//2
            if nums[mid]<0:
                l=mid+1
            else:
                r=mid
        neg=l
        
        return max(pos,neg)