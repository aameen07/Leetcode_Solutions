class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        length=len(nums)
        nums.sort()
                
        return ((nums[length-1]*nums[length-2]) - (nums[0]*nums[1]))