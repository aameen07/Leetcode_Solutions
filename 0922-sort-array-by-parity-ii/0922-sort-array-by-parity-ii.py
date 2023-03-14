class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        i=0
        j=1
        
        while(i<len(nums)):
            
            if nums[i]%2==0:
                i+=2
            elif nums[j]%2!=0:
                j+=2
            else:
                nums[j],nums[i]=nums[i],nums[j]
                i+=2
                j+=2
            
            
        
        return nums