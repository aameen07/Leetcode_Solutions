class Solution:
    def letterCombinations(self, nums: str) -> List[str]:
        dic = {"2":"abc",
               "3":"def",
               "4":"ghi", 
               "5":"jkl", 
               "6":"mno", 
               "7":"pqrs", 
               "8":"tuv", 
               "9":"wxyz"}

        res=[]
        if len(nums)==0:
            return res

        self.dfs(nums,0,dic,"",res)
        return res

    def dfs(self,nums,index,dic,path,res):
        if index==len(nums):
            res.append(path)
            return

        string=dic[nums[index]]

        for i in string:
            self.dfs(nums,index+1,dic,path+i,res)