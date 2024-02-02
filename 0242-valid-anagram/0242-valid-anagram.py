class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t): return False
        
        d={}
        for i in s:
            if i in d: d[i]+=1
            else: d[i]=1
                
        for j in t:
            if j in d: d[j]-=1
            else: return False

        for k,v in d.items():
            if v!=0: return False
        
        return True
    
    
# 