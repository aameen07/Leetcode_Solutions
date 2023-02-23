class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        total = sum(nums)
        n=len(nums)
        wholeTotal= ((n) * (n+1)//2)
        
        return wholeTotal-total
        