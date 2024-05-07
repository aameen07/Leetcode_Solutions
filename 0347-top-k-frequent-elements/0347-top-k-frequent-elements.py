class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num=Counter(nums)
        return sorted(num, key=num.get, reverse=True)[:k]
    
    
# The counter gets the nums values as keys with their count as the values. Then in sorted we take that dic and give num.get so that it chooses values of dic as the basis of sorting and then reverse the sorted array. now [:k] this was given to slice and return only the k elements of the array