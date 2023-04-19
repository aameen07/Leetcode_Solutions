class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        res=[-1]*len(nums)
        # print(res)
        stack=[]
        for i in range(len(nums)):
            while stack and nums[i]>nums[stack[-1]]:
                res[stack.pop()]=nums[i]
            stack.append(i)
        # print(stack)
        # print(res)
        
        # for j in range(len(stack)-1,-1,-1):
        for i in range(len(nums)):
            while stack and nums[i]>nums[stack[-1]]:
                res[stack.pop()]=nums[i]
        return res