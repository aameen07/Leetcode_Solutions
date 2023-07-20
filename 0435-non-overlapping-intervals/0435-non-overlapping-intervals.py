class Solution:
    def eraseOverlapIntervals(self, nums: List[List[int]]) -> int:
        c=0
        prev=0
        nums = sorted(nums, key = lambda x: x[1])
        for i in range (1,len(nums)):
            if nums[prev][1] > nums[i][0]:
                c+=1
            else:
                prev = i
        
        return c
        
        
        