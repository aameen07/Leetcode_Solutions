class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        strnum=list(str(num))
        c=0
        
        for i in range(len(strnum)-k+1):
            a= strnum[i:i+k]    
            a=int("".join(a))
            if a!=0 and num % a == 0:
                c+=1
                
        return c