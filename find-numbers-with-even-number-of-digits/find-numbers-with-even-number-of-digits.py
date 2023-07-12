class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res=0
        c=0
        for i in nums:
            while i:
                i=i//10
                c+=1
            if c%2==0:
                res+=1
            c=0
        return res