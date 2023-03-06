class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            m=(l+r)//2
            
            if nums[m]-m-1 < k:
                l=m+1
            else:
                r=m-1
        
        return l+k