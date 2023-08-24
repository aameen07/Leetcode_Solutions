class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res=1
        c=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                c+=1
            else:
                c=1
            res=max(res,c)
        
        return res