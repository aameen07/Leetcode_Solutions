class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        l=0
        
        for r in range(1,len(nums)):
            if (nums[l]%2==0):
                l+=1
            elif nums[l]%2!=0 and nums[r]%2==0:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                
        return nums
        