class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # nums.sort()
        # result=[[]]
        # for i in nums:
        #     result+=[s+[i] for s in result]
        # return result
        
        
        # or
        
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self,nums,path,res):
        res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:],path+[nums[i]],res)

