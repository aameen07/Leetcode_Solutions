class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        
        res = ""
        i=0
        j=0
        
        while (i<len(w1) or j<len(w2)):
            
            if i<len(w1):
                res+=w1[i]
                i+=1
            
            if j<len(w2):
                res+=w2[j]
                j+=1
        
        return res
            