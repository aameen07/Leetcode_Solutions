class Solution:
    def removeStars(self, s: str) -> str:
        i=0
        a=[]
        while(i<len(s)):
            if s[i]!="*":
                a.append(s[i])
            else:
                a.pop()
            i+=1
            # print(a)
        return "".join(a)
        