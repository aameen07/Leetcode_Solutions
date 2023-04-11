class Solution:
    def removeStars(self, s: str) -> str:
        i=0
        a=""
        while(i<len(s)):
            if s[i]!="*":
                a+=(s[i])
            else:
                a=a[:-1]
            i+=1
            
        return a
        