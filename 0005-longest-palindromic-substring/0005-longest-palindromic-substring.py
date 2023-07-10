class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.long = ""
        self.llen = 0
        for i in range(len(s)):
            self.isValid(s,i,i)
            self.isValid(s,i,i+1)
        return self.long
    
    def isValid(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            if self.llen<(r-l+1):
                self.llen=r-l+1
                self.long=s[l:r+1]
            l-=1
            r+=1