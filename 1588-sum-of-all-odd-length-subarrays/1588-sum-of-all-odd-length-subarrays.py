class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total=0
        for i in range(len(arr)): # 1
            for j in range(i,len(arr),2): #1,3
                total+=sum(arr[i:j+1])      #1 11
        
        return total
            