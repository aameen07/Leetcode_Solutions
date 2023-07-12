class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=0
        r=n-1
        res=[0]*n
        k=n-1
        while l<=r:
            if abs(nums[l]) < abs(nums[r]):
                res[k]= nums[r]**2
                r-=1
            else:
                res[k]= nums[l]**2
                l+=1
            k-=1
        return res