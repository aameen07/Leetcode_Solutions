class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        k=k % len(nums)
        if k>0:
            nums[:]=nums[-k:]+nums[:-k]
        
          
            
        """
        Do not return anything, modify nums in-place instead.
        """
        