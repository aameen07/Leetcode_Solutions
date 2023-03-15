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
    
        # we'll use index and try to find non zero values and we put them in index postion then increment index and in the end we just put zeros in the remaining postions.    