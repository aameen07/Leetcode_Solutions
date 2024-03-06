class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total=sum(nums)
        lsum=rsum=0
        pivotIndex=0
        
        for i in range(len(nums)):

            rsum=total-nums[pivotIndex]-lsum
            print(lsum,rsum)
            if lsum == rsum:        
                return i
            
            lsum+=nums[pivotIndex]
            pivotIndex+=1
        
        return -1
        