class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i=0 #zeros
        j=0 #nonzeros
        while (j<len(nums)):
            
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1
                   
        
        
        
        
        
        
#         index=0
#         for i in nums:
#             if i!=0:
#                 nums[index]=i
#                 index+=1
        
#         for j in range(index,len(nums)):
#             nums[j]=0
            
#         return nums
    
        # we'll use index and try to find non zero values and we put them in index postion then increment index and in the end we just put zeros in the remaining postions.    
        
        
        
        
#         index = 0 
#         for i in nums:
#             if i != 0:                  #we check if the item is non-zero value
#                 nums[index]=i
#                 index+=1
#         for j in range(index, len(nums)):       #in this loop we're putting zero in the remaining  
#                                                 #ending length of the loop
#             nums[j]=0                   
        
#         return nums


        # if len(nums)==0: return nums      #simply checks if the list is empty
        # for i in nums:
        #     if i == 0:
        #         nums.remove(i)         #we remove it and append it in end
        #         nums.append(i)
        #     else:
        #         continue       # if its not 0 value in the list we continue
        # return nums