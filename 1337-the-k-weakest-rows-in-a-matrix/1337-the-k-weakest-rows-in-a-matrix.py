class Solution:
    def kWeakestRows(self, nums: List[List[int]], k: int) -> List[int]:
        arr=[]
        
        for i, val in enumerate(nums):
            arr.append([sum(val),i])    #we take the pairs of sum and index
            
        arr.sort(key=lambda c : (c[0],c[1]))   # it will sort first acc to sum and if sum is equal then acc to                                                  indexes in that particular case
        return [i for _, i in arr[:k]]          # we need only k indexes and they are already in weakest to                                                     strongest form now
        