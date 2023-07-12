class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        res=0
        for i,val in enumerate(nums):
            if val==1:
                c+=1
                res=max(res,c)
            else:
                c=0
        return res