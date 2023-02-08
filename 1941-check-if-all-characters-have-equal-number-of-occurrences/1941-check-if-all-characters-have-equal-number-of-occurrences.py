class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        a=0
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            
            if a==0 or d[i]>a:
                a=d[i]
            

        for j in d:
            
            if a!=d[j]:
                return False
        
        return True
            
            
            
            