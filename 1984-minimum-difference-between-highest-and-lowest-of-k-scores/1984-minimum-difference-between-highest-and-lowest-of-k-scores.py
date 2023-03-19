class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        # print(nums)
        mini=float('inf')
        l=0
        r=k-1
        while(r<len(nums)):
            if nums[r]-nums[l]<mini:
                mini=nums[r]-nums[l]
            # print(mini)
            l+=1
            r+=1
        
        return mini
            
            