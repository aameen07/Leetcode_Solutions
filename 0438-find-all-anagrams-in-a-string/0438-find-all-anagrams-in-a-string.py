class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p)>len(s):
            return []
        
        a=[0]*26
        res = []
        
        for i in range(len(p)):
            a[ord(p[i])-ord("a")]+=1  
            a[ord(s[i])-ord("a")]-=1   
            
            
        if a==[0]*26:
            res.append(0)
            
        for j in range(len(p),len(s)):
            a[ord(s[j-len(p)])-ord("a")]+=1
            a[ord(s[j])-ord("a")]-=1
            
            if a==[0]*26:
                res.append(j-len(p)+1)
                  
        return res
