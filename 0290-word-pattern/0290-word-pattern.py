class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        p=list(pattern)
        s=s.split()
        d={}
        
        if len(s)!=len(p): return False
        if len(set(s))!=len(set(p)): return False
        
        for i , val in enumerate(p):
            if val in d and d[val]!=s[i]:
                return False
            else:
                d[val]=s[i]
                
        return True

        