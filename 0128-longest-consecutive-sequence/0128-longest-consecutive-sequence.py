class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        longest = 0
        
        for n in nums:
            if n-1 not in numset:
                length=0
                while (n+length) in numset:
                    length+=1
                
                longest=max(length,longest)
        
        return longest
        
# We have to take a integer that holds our result and a resettable integer that holds the current Consecutive Sequence length. so we make a set and then go through nums and then check if that value is the starting of a new sequence and then we check if the next element is there or not and keep checking that and later we check which is maximum the length or the last longest. and give longest in the end