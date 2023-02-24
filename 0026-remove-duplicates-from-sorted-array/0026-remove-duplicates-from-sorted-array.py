class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length=0
        n=len(nums)
        
        # if n<0: return length
        
        for i in range(1,n):
            if nums[length] != nums[i]:
                length+=1
                nums[length]=nums[i]
                
        return length+1

        