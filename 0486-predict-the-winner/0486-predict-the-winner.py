class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        a = self.helper(nums,0,len(nums)-1)
        return a >= sum(nums)-a
    
    def helper(self, nums, i, j):
        if i>j:
            return 0
        if i == j:
            return nums[i]
        
        left = nums[i] + min(self.helper(nums,i+2,j),self.helper(nums,i+1,j-1))
        right = nums[j] + min(self.helper(nums,i+1,j-1),self.helper(nums,i,j-2))
        
        return max(left, right)
    
        # max1 = nums[i] - self.helper(nums,i+1,j)
        # max2 = nums[j] - self.helper(nums,i,j-1)
        
        
        