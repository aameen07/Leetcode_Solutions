class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0 
        for i in nums:
            if i != 0:                  #we check if the item is non-zero value
                nums[index]=i
                index+=1
        for j in range(index, len(nums)):       #in this loop we're putting zero in the remaining  
                                                #ending length of the loop
            nums[j]=0                   
        
        return nums


        # if len(nums)==0: return nums      #simply checks if the list is empty
        # for i in nums:
        #     if i == 0:
        #         nums.remove(i)         #we remove it and append it in end
        #         nums.append(i)
        #     else:
        #         continue       # if its not 0 value in the list we continue
        # return nums