class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        

        up=down=0
        for i in range (1,len(nums)):
            if nums[i-1]<nums[i]:
                up=down+1
            elif nums[i-1]>nums[i]:
                down=up+1
        
        return 1+max(up,down)
        