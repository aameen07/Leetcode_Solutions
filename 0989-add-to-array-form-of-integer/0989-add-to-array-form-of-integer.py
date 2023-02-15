class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        
        for i in range(len(num)-1,-1,-1):
            a = num[i] + k
            num[i] = a % 10
            k = a // 10
            
        while(k):
            a=k%10
            num.insert(0,a)
            k=k//10
            
        return num
            
        
        