class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        l1=[]
        for i in range(len(nums)):
            l1.insert(index[i],nums[i])
        return l1
        