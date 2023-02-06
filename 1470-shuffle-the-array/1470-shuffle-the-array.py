class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i, j in zip(nums[:n],nums[n:]):
            res += [i,j]
        return res

# this one is simply extending the list with 2 values at the same time aur baakki dono bhi aisi kr rhe hai but ye shyd sirf integer wali list pr kaam aaenge ye programs

#         out = []
#         for i in range(n):
#             out.extend((nums[i], nums[i+n]))                 
#         return out
  
#         p1 = 0
#         ans = []
#         while ((p1+n) < (2*n)):
#             ans += [nums[p1], nums[p1 + n]]
#             p1 += 1
#         return ans
    