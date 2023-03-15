class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        index=0
        for i in nums:
            if i!=0:
                nums[index]=i
                index+=1
        
        for j in range(index,len(nums)):
            nums[j]=0
        
            
            
                
        return nums
    
        # we're using i to catch zeros in the nums and we're using j to catch non zero values and then we just swap them and move ahead. 
    