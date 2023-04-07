class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        avg=presum=sum(nums[:k])
        
        for i in range(1,len(nums)-k+1):
            presum+=-nums[i-1]+nums[i+k-1]
            avg=max(avg,presum)
        
        return avg/k
            
        