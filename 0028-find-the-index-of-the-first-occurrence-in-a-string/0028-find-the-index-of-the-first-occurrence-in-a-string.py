class Solution:
    def strStr(self, h: str, n: str) -> int:
        
        if h==n:
            return 0
        l=0
        for r in range(len(n)-1,len(h)):
            if h[l:r+1]==n:
                return l
            else:
                l+=1
        return -1
        
        
