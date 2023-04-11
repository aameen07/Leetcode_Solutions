class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        
        res=[]
        lsum=[0]
        rsum=[0]
        
        for num in nums[:-1]:
            lsum.append(lsum[-1]+num)
        for num in nums[::-1][:-1]:
            rsum.insert(0,rsum[0]+num)
        for i in range(len(nums)):
            res.append(abs(lsum[i]-rsum[i]))
        return res
        
        
#         rsum=sum(list(nums[1:]))
#         lsum=0
#         ans=[rsum]
#         for i in range(1,len(nums)):
#             rsum=rsum-nums[i]
#             lsum=lsum+nums[i-1]
#             a=abs(lsum-rsum)
#             ans+=[a]
        
#         return ans

        
    