class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        return len(nums) != len(set(nums))
    
        # or
        # return True if len(set(nums)) < len(nums) else False
        # or
        
        # d={}
        # for i in nums:
        #     if i not in d:
        #         d[i]=1
        #     else:
        #         return True
        # return False
        
        
# Just need to return true if any value is more than once.
# We can also just compare normal len and set len.