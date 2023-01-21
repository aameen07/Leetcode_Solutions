class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l1=[]
        for i in range (0,len(nums),2):
            for j in range(nums[i]):
                l1.append(nums[i+1])
            
        return l1