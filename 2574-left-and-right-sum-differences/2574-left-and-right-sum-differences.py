class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        
        rsum=sum(list(nums[1:]))
        
        lsum=0
        ans=[rsum]
        for i in range(1,len(nums)):
            rsum=rsum-nums[i]
            lsum=lsum+nums[i-1]
            a=abs(lsum-rsum)
            ans+=[a]
            # print(ans)
        
        return ans