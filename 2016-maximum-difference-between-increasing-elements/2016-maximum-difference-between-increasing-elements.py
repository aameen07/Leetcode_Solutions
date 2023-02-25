class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        value=-1
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    value=max(nums[j]-nums[i], value)
        return value