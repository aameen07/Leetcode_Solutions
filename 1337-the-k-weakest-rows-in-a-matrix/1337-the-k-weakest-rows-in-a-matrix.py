class Solution:
    def kWeakestRows(self, nums: List[List[int]], k: int) -> List[int]:
        arr=[]
        for i, val in enumerate(nums):
            arr.append([sum(val),i])
            
        arr.sort(key=lambda c : (c[0],c[1]))
        
        return [i for _, i in arr[:k]]
        