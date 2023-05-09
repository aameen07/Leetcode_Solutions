class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        p=list(pattern)
        s=s.split()
        print(p)
        print(s)
        
        d={}
        
        if len(p)!=len(s): return False
        if len(set(p))!=len(set(s)): return False
        
        for i, val in enumerate(p):
            if val in d and d[val]!=s[i]:
                return False
            else:
                d[val]=s[i]
        
        return True
